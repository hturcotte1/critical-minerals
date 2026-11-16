// Print an HTML file to PDF with headless Chromium (Playwright).
// Usage: node tools/print_pdf.js <input.html> <output.pdf> <Letter|Tabloid|A4> <portrait|landscape> "<footer title>"
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const [, , input, output, format, orientation, title] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(input), { waitUntil: 'load' });
  const esc = (s) => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;');
  await page.pdf({
    path: output,
    format: format || 'Letter',
    landscape: orientation === 'landscape',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate:
      '<div style="font-family: Liberation Sans, DejaVu Sans, Arial, sans-serif; font-size:7px; color:#666; width:100%; padding:0 10mm; display:flex; justify-content:space-between;">' +
      '<span>' + esc(title) + '</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>',
    margin: { top: '11mm', bottom: '13mm', left: '10mm', right: '10mm' },
  });
  await browser.close();
  console.log('wrote ' + output);
})();
