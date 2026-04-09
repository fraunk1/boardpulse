#!/usr/bin/env python3
"""
RI_MD final scraper — Full pipeline:
1. Paginate both Past Meetings and Recently Filed Minutes tables
2. Call ViewMeetingDetailByID AJAX for each meeting
3. Parse DownloadMeetingFiles() onclick patterns for agenda/minutes PDFs
4. Download files from /Common/DownloadMeetingFiles?FilePath=
5. Save to boardpulse.db
"""

import asyncio
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import httpx
from dateutil import parser as dateparser
from playwright.async_api import async_playwright

BASE = Path('/Users/frankmeyers/Desktop/Claude Code/Projects/boardpulse')
DB = BASE / 'boardpulse.db'
DOCS_DIR = BASE / 'data' / 'documents'
SCREENSHOTS_DIR = BASE / 'data' / 'screenshots'

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
BOARD_CODE = 'RI_MD'
BASE_URL = 'https://opengov.sos.ri.gov'
DOWNLOAD_URL = f'{BASE_URL}/Common/DownloadMeetingFiles?FilePath='


def get_board_id() -> int:
    conn = sqlite3.connect(str(DB))
    row = conn.execute('SELECT id FROM boards WHERE code = ?', (BOARD_CODE,)).fetchone()
    conn.close()
    return row[0]


def parse_opengov_date(date_str: str) -> str | None:
    date_str = date_str.strip()
    m = re.match(r'^\d{14}(.+)$', date_str)
    if m:
        date_str = m.group(1).strip()
    m = re.match(r'^(\d{1,2})/(\d{1,2})/(\d{4})$', date_str)
    if m:
        return f'{int(m.group(3)):04d}-{int(m.group(1)):02d}-{int(m.group(2)):02d}'
    try:
        parsed = dateparser.parse(date_str)
        if parsed:
            return parsed.strftime('%Y-%m-%d')
    except Exception:
        pass
    return None


def save_meeting(board_id: int, meeting_date: str, title: str, source_url: str = None) -> int:
    conn = sqlite3.connect(str(DB))
    conn.execute('PRAGMA busy_timeout = 30000')
    existing = conn.execute(
        'SELECT id FROM meetings WHERE board_id = ? AND meeting_date = ?',
        (board_id, meeting_date)
    ).fetchone()
    if existing:
        mid = existing[0]
    else:
        conn.execute(
            'INSERT INTO meetings (board_id, meeting_date, title, source_url, scraped_at) VALUES (?, ?, ?, ?, ?)',
            (board_id, meeting_date, title, source_url, datetime.now(timezone.utc).isoformat())
        )
        mid = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
    conn.commit()
    conn.close()
    return mid


def save_document(meeting_id: int, doc_type: str, filename: str, filepath: str, source_url: str) -> bool:
    conn = sqlite3.connect(str(DB))
    conn.execute('PRAGMA busy_timeout = 30000')
    existing = conn.execute(
        'SELECT id FROM meeting_documents WHERE meeting_id = ? AND source_url = ?',
        (meeting_id, source_url)
    ).fetchone()
    if existing:
        conn.close()
        return False
    conn.execute(
        'INSERT INTO meeting_documents (meeting_id, doc_type, filename, file_path, source_url, scraped_at) VALUES (?, ?, ?, ?, ?, ?)',
        (meeting_id, doc_type, filename, filepath, source_url, datetime.now(timezone.utc).isoformat())
    )
    conn.commit()
    conn.close()
    return True


async def collect_meeting_ids(page, table_id: str) -> list[dict]:
    """Paginate a DataTable and collect all rows with meeting IDs."""
    # Set to 100 entries per page
    await page.evaluate(f'''() => {{
        const table = document.getElementById("{table_id}");
        if (!table) return;
        const wrapper = table.closest(".dataTables_wrapper");
        if (!wrapper) return;
        const select = wrapper.querySelector("select[name='{table_id}_length']");
        if (select) {{ select.value = "100"; select.dispatchEvent(new Event("change")); }}
    }}''')
    await page.wait_for_timeout(3000)

    all_entries = []
    seen = set()
    page_num = 0

    while True:
        rows = await page.evaluate(f'''() => {{
            const table = document.getElementById("{table_id}");
            if (!table) return [];
            const result = [];
            for (const tr of table.querySelectorAll("tbody tr")) {{
                const cells = Array.from(tr.querySelectorAll("td")).map(td => td.textContent.trim());
                let meetingId = null;
                const html = tr.outerHTML;
                const match = html.match(/ViewMeetingDetails\\((\\d+)\\)/);
                if (match) meetingId = match[1];
                result.push({{meetingId, cells}});
            }}
            return result;
        }}''')

        new_count = 0
        for row in rows:
            mid = row.get('meetingId')
            key = mid or '|'.join(row['cells'])
            if key not in seen:
                seen.add(key)
                all_entries.append(row)
                new_count += 1

        page_num += 1
        if new_count == 0:
            break

        has_next = await page.evaluate(f'''() => {{
            const table = document.getElementById("{table_id}");
            if (!table) return false;
            const wrapper = table.closest(".dataTables_wrapper");
            if (!wrapper) return false;
            const next = wrapper.querySelector(".paginate_button.next:not(.disabled)");
            if (next) {{ next.click(); return true; }}
            return false;
        }}''')
        if not has_next:
            break
        await page.wait_for_timeout(1500)
        if page_num > 15:
            break

    print(f'  {table_id}: {len(all_entries)} entries across {page_num} pages')
    return all_entries


async def scrape():
    board_id = get_board_id()
    url = f'{BASE_URL}/OpenMeetingsPublic/OpenMeetingDashboard?subtopmenuId=201&EntityID=1906'
    doc_dir = DOCS_DIR / BOARD_CODE
    doc_dir.mkdir(parents=True, exist_ok=True)

    print(f'RI_MD Scraper — {datetime.now().isoformat()}\n')

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent=UA, viewport={'width': 1920, 'height': 1080})
        page = await context.new_page()

        await page.goto(url, wait_until='domcontentloaded', timeout=60000)
        await page.wait_for_timeout(15000)

        # ---- Collect meeting IDs from both tables ----
        print('Collecting meeting IDs...')
        past_entries = await collect_meeting_ids(page, 'YesterDayEntitiesSummary')
        filed_entries = await collect_meeting_ids(page, 'RecentlyFiledMeetingMinutes')

        # Merge: build unique set of (meeting_id, date, time)
        all_meetings = {}  # meeting_opengov_id -> {date, time}
        date_only_meetings = []  # meetings without IDs

        for entry in past_entries + filed_entries:
            mid = entry.get('meetingId')
            cells = entry.get('cells', [])
            date_str = cells[0] if cells else ''
            time_str = cells[1] if len(cells) > 1 else ''

            if mid:
                if mid not in all_meetings:
                    all_meetings[mid] = {'date': date_str, 'time': time_str}
            else:
                date_only_meetings.append({'date': date_str, 'time': time_str})

        print(f'\nUnique meetings with IDs: {len(all_meetings)}')
        print(f'Meetings without IDs: {len(date_only_meetings)}')

        # ---- Save all meetings to DB first ----
        print('\nSaving meetings to DB...')
        meetings_saved = 0
        for mid, info in all_meetings.items():
            date = parse_opengov_date(info['date'])
            if not date:
                continue
            display_date = re.sub(r'^\d{14}', '', info['date']).strip()
            display_time = re.sub(r'^\d{6}', '', info['time']).strip()
            title = f'Board Meeting - {display_date}'
            if display_time:
                title += f' {display_time}'
            save_meeting(board_id, date, title, source_url=f'{url}&MeetingID={mid}')
            meetings_saved += 1

        for info in date_only_meetings:
            date = parse_opengov_date(info['date'])
            if not date:
                continue
            display_date = re.sub(r'^\d{14}', '', info['date']).strip()
            display_time = re.sub(r'^\d{6}', '', info['time']).strip()
            title = f'Board Meeting - {display_date}'
            if display_time:
                title += f' {display_time}'
            save_meeting(board_id, date, title, source_url=url)
            meetings_saved += 1

        print(f'Meetings saved: {meetings_saved}')

        # ---- Fetch detail for each meeting with ID ----
        print(f'\nFetching meeting details and downloading documents...')

        docs_downloaded = 0
        agendas_found = 0
        minutes_found = 0

        meeting_items = list(all_meetings.items())
        for i, (mid, info) in enumerate(meeting_items):
            date = parse_opengov_date(info['date'])
            if not date:
                continue

            # AJAX call to get meeting detail HTML
            raw_html = await page.evaluate(f'''() => {{
                return new Promise((resolve) => {{
                    $.ajax({{
                        url: '/OpenMeetingsPublic/ViewMeetingDetailByID?id=' + Math.random(),
                        data: {{ MeetingID: {mid} }},
                        type: 'GET',
                        success: function(data) {{ resolve(data); }},
                        error: function(xhr, status, error) {{ resolve(null); }}
                    }});
                }});
            }}''')

            if not raw_html:
                continue

            # Parse DownloadMeetingFiles patterns
            file_matches = re.findall(
                r"DownloadMeetingFiles\('([^']+)'\).*?>(.*?)</a>",
                raw_html, re.DOTALL
            )

            display_date = re.sub(r'^\d{14}', '', info['date']).strip()
            display_time = re.sub(r'^\d{6}', '', info['time']).strip()
            title = f'Board Meeting - {display_date}'
            if display_time:
                title += f' {display_time}'

            meeting_db_id = save_meeting(board_id, date, title,
                                          source_url=f'{url}&MeetingID={mid}')

            for file_path, link_text in file_matches:
                # Clean the path (unescape backslashes)
                clean_path = file_path.replace('\\\\', '\\')
                download_url = DOWNLOAD_URL + clean_path
                link_text_clean = link_text.strip()

                # Determine doc type from path and text
                if 'Minutes' in clean_path or 'minute' in link_text_clean.lower():
                    doc_type = 'minutes'
                    minutes_found += 1
                elif 'Notices' in clean_path or 'agenda' in link_text_clean.lower():
                    doc_type = 'agenda'
                    agendas_found += 1
                else:
                    doc_type = 'other'

                # Create filename
                safe_text = re.sub(r'[^\w\-]', '_', link_text_clean[:40])
                filename = f'{date}_{doc_type}_{safe_text}.pdf'
                filepath = doc_dir / filename

                # Download if not cached
                if not filepath.exists():
                    try:
                        resp = httpx.get(download_url, follow_redirects=True, timeout=30,
                                         headers={'User-Agent': UA})
                        resp.raise_for_status()
                        if len(resp.content) > 100:  # Skip empty/error responses
                            filepath.write_bytes(resp.content)
                        else:
                            continue
                    except Exception as e:
                        if i < 5:
                            print(f'    Download error for {download_url}: {e}')
                        continue

                # Save document record
                if save_document(meeting_db_id, doc_type, filename, str(filepath), download_url):
                    docs_downloaded += 1

            if (i + 1) % 25 == 0:
                print(f'  Progress: {i+1}/{len(meeting_items)} meetings | {docs_downloaded} docs ({minutes_found} minutes, {agendas_found} agendas)')

        print(f'\nComplete: {docs_downloaded} documents downloaded ({minutes_found} minutes, {agendas_found} agendas)')

        # Final screenshot
        await page.goto(url, wait_until='domcontentloaded', timeout=30000)
        await page.wait_for_timeout(5000)
        await page.screenshot(path=str(SCREENSHOTS_DIR / f'{BOARD_CODE}_final.png'), full_page=True)

        await browser.close()

    # ---- Final report ----
    conn = sqlite3.connect(str(DB))
    total = conn.execute('SELECT COUNT(*) FROM meetings WHERE board_id = ?', (board_id,)).fetchone()[0]
    total_docs = conn.execute('''
        SELECT COUNT(*) FROM meeting_documents md
        JOIN meetings m ON md.meeting_id = m.id WHERE m.board_id = ?
    ''', (board_id,)).fetchone()[0]
    min_date = conn.execute('SELECT MIN(meeting_date) FROM meetings WHERE board_id = ?', (board_id,)).fetchone()[0]
    max_date = conn.execute('SELECT MAX(meeting_date) FROM meetings WHERE board_id = ?', (board_id,)).fetchone()[0]

    minutes_count = conn.execute('''
        SELECT COUNT(*) FROM meeting_documents md
        JOIN meetings m ON md.meeting_id = m.id
        WHERE m.board_id = ? AND md.doc_type = 'minutes'
    ''', (board_id,)).fetchone()[0]

    agenda_count = conn.execute('''
        SELECT COUNT(*) FROM meeting_documents md
        JOIN meetings m ON md.meeting_id = m.id
        WHERE m.board_id = ? AND md.doc_type = 'agenda'
    ''', (board_id,)).fetchone()[0]

    print(f'\n{"="*60}')
    print(f'RI_MD FINAL RESULTS')
    print(f'{"="*60}')
    print(f'Meetings: {total} (range: {min_date} to {max_date})')
    print(f'Documents: {total_docs} total ({minutes_count} minutes, {agenda_count} agendas)')

    # Show recent meetings with docs
    samples = conn.execute('''
        SELECT m.meeting_date, m.title,
            GROUP_CONCAT(md.doc_type || ':' || md.filename, ' | ') as docs
        FROM meetings m
        LEFT JOIN meeting_documents md ON md.meeting_id = m.id
        WHERE m.board_id = ?
        GROUP BY m.id
        ORDER BY m.meeting_date DESC LIMIT 20
    ''', (board_id,)).fetchall()

    print('\nRecent meetings:')
    for date, title, docs in samples:
        doc_info = f' -> {docs}' if docs else ' (no docs)'
        print(f'  {date}: {title[:50]}{doc_info[:80]}')

    conn.close()


async def main():
    await scrape()
    print(f'\nDone: {datetime.now().isoformat()}')


if __name__ == '__main__':
    asyncio.run(main())
