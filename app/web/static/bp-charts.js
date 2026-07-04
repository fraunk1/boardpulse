/* boardpulse — shared ApexCharts configuration.
 *
 * Loaded only on /trends and /topic (via {% block head %}), never in
 * base.html. Every chart on the page pulls its base look from here so the
 * palette, type, and interaction feel stay consistent.
 *
 * Usage:
 *   const opts = BPCharts.merge(BPCharts.base(), { series: [...], ... });
 *   new ApexCharts(el, opts).render();
 */
(function () {
    // FSMB / boardpulse palette — teal-forward, gold accent, navy structure.
    const PALETTE = ['#139AD0', '#FBAA29', '#1B2636', '#576A83', '#3DB8E5', '#FCC254'];

    const FONT = '"DM Sans", system-ui, -apple-system, sans-serif';

    // Shared base: animations off (dense page, no motion noise), toolbar off,
    // clean grid, DM Sans everywhere.
    function base() {
        return {
            chart: {
                fontFamily: FONT,
                foreColor: '#576A83',
                toolbar: { show: false },
                zoom: { enabled: false },
                animations: { enabled: false },
                parentHeightOffset: 0,
            },
            colors: PALETTE.slice(),
            grid: {
                borderColor: '#DCE3ED',
                strokeDashArray: 3,
                padding: { left: 8, right: 8, top: 0, bottom: 0 },
            },
            dataLabels: { enabled: false },
            legend: {
                fontSize: '12px',
                fontWeight: 500,
                labels: { colors: '#576A83' },
                markers: { width: 10, height: 10, radius: 3 },
                itemMargin: { horizontal: 8, vertical: 2 },
            },
            tooltip: {
                style: { fontSize: '12px', fontFamily: FONT },
                theme: 'light',
            },
            xaxis: {
                labels: { style: { colors: '#97A8BD', fontSize: '11px' } },
                axisBorder: { color: '#DCE3ED' },
                axisTicks: { color: '#DCE3ED' },
            },
            yaxis: {
                labels: { style: { colors: '#97A8BD', fontSize: '11px' } },
            },
            states: {
                hover: { filter: { type: 'lighten', value: 0.06 } },
                active: { filter: { type: 'darken', value: 0.1 } },
            },
        };
    }

    // Shallow-ish recursive merge: override wins, plain objects merge, arrays
    // and scalars are replaced. Enough for chart option composition.
    function merge(target, override) {
        const out = Array.isArray(target) ? target.slice() : Object.assign({}, target);
        for (const key of Object.keys(override || {})) {
            const ov = override[key];
            const tv = out[key];
            if (ov && typeof ov === 'object' && !Array.isArray(ov)
                && tv && typeof tv === 'object' && !Array.isArray(tv)) {
                out[key] = merge(tv, ov);
            } else {
                out[key] = ov;
            }
        }
        return out;
    }

    window.BPCharts = { PALETTE: PALETTE, FONT: FONT, base: base, merge: merge };
})();
