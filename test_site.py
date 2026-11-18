import os
import pathlib
import unittest
from playwright.sync_api import sync_playwright

SITE = pathlib.Path(__file__).with_name('index.html')

class SiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p = sync_playwright().start()
        executable = os.environ.get('CHROMIUM_EXECUTABLE')
        cls.browser = cls.p.chromium.launch(**({'executable_path': executable} if executable else {}), args=['--no-sandbox'])

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.p.stop()

    def page(self, width=1280, color_scheme='light'):
        page = self.browser.new_page(viewport={'width': width, 'height': 800}, color_scheme=color_scheme)
        self.addCleanup(page.close)
        page.goto(SITE.as_uri())
        return page

    def test_navigation_and_research_status(self):
        page = self.page()
        page.locator('.technical-example summary').click()
        self.assertEqual(page.locator('main section').count(), 6)
        self.assertIn('Forschungsprojekt', page.locator('h1').inner_text())
        self.assertIn('Simulation', page.locator('#demo').inner_text())
        self.assertIn('keine fertige', page.locator('#forschung').inner_text())
        self.assertTrue(page.get_by_role('heading', name='Was soll gefördert werden?').is_visible())
        self.assertIn('Nicht Gegenstand der Förderung', page.locator('#loesung').inner_text())
        self.assertIn('Diese Website erkennt keine PDFs', page.locator('#demo').inner_text())
        for link in page.locator('nav a[href^="#"]').all():
            self.assertEqual(page.locator(link.get_attribute('href')).count(), 1)

    def test_mapping_requires_human_confirmation(self):
        page = self.page()
        page.locator('.technical-example summary').click()
        button = page.get_by_role('button', name='Zuordnung bestätigen')
        self.assertTrue(button.is_disabled())
        page.get_by_label('Ziel auswählen').select_option('applicant')
        self.assertTrue(button.is_enabled())
        self.assertFalse(page.locator('#result').is_visible())
        button.click()
        self.assertIn('Antragstellende Person', page.locator('#result').inner_text())
        page.get_by_role('button', name='Zurücksetzen').click()
        self.assertTrue(button.is_disabled())
        self.assertFalse(page.locator('#result').is_visible())

    def test_unmapped_does_not_export_value(self):
        page = self.page()
        page.locator('.technical-example summary').click()
        page.get_by_label('Ziel auswählen').select_option('unknown')
        page.get_by_role('button', name='Zuordnung bestätigen').click()
        self.assertIn('Keine Zuordnung', page.locator('#result').inner_text())
        self.assertNotIn('Alex Muster', page.locator('#result').inner_text())

    def test_conflicting_section_does_not_export_value(self):
        page = self.page()
        page.locator('.technical-example summary').click()
        page.get_by_label('Ziel auswählen').select_option('household')
        page.get_by_role('button', name='Zuordnung bestätigen').click()
        result = page.locator('#result').inner_text()
        self.assertIn('Widerspruch', result)
        self.assertIn('Keine Ausgabe', result)
        self.assertNotIn('Alex Muster', result)

    def test_mobile_no_horizontal_overflow_or_external_requests(self):
        page = self.browser.new_page(viewport={'width': 360, 'height': 800})
        self.addCleanup(page.close)
        network = []
        errors = []
        page.on('request', lambda r: network.append(r.url) if r.url.startswith(('http:', 'https:')) else None)
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.goto(SITE.as_uri())
        self.assertLessEqual(page.evaluate('document.documentElement.scrollWidth'), 360)
        self.assertEqual(network, [])
        self.assertEqual(errors, [])

    def test_story_animation_shows_paper_detour_then_digital_signing(self):
        page = self.page()
        page.clock.install()
        page.get_by_role('button', name='Animation neu starten').click()
        active = page.locator('#story [aria-current="step"]')
        self.assertTrue(page.locator('#story-stage').is_visible())
        self.assertEqual(page.locator('#story-art svg').count(), 1)
        self.assertEqual(page.locator('#story-chapter').text_content(), 'Heute · 1 / 5')
        self.assertIn('Formular herunterladen', page.locator('#story-title').inner_text())
        self.assertIn('Herunterladen', active.inner_text())
        self.assertNotEqual(page.locator('#story-art .person-arm').evaluate('(el) => getComputedStyle(el).animationName'), 'none')
        for expected in ('Ausdrucken', 'Unterschreiben', 'Einscannen', 'Abschicken'):
            page.clock.run_for(2400)
            self.assertIn(expected, active.inner_text())
        page.clock.run_for(2400)
        self.assertTrue(page.locator('#paper-cross').is_visible())
        self.assertEqual(page.locator('#story-stage').get_attribute('data-phase'), 'transition')
        page.clock.run_for(2400)
        self.assertIn('Herunterladen', active.inner_text())
        self.assertEqual(page.locator('#story-chapter').text_content(), 'Zukunftsvision · 1 / 3')
        page.clock.run_for(2400)
        self.assertIn('Auf dem Display unterschreiben', active.inner_text())
        self.assertNotEqual(page.locator('#story-art .finger').evaluate('(el) => getComputedStyle(el).animationName'), 'none')
        self.assertNotEqual(page.locator('#story-art .signature').evaluate('(el) => getComputedStyle(el).animationName'), 'none')
        page.clock.run_for(2400)
        self.assertIn('Digital abschicken', active.inner_text())
        page.clock.run_for(2400)
        self.assertTrue(page.locator('#story-done').is_visible())
        self.assertEqual(page.locator('#story-stage').get_attribute('data-phase'), 'finish')

    def test_story_pause_and_restart(self):
        page = self.page()
        page.clock.install()
        page.get_by_role('button', name='Animation neu starten').click()
        page.get_by_role('button', name='Animation anhalten').click()
        page.clock.run_for(4000)
        self.assertIn('Herunterladen', page.locator('#story [aria-current="step"]').inner_text())
        page.get_by_role('button', name='Animation fortsetzen').click()
        page.clock.run_for(2400)
        self.assertIn('Ausdrucken', page.locator('#story [aria-current="step"]').inner_text())

    def test_story_does_not_reuse_unversioned_cached_demo_script(self):
        page = self.browser.new_page(viewport={'width': 1280, 'height': 800})
        self.addCleanup(page.close)
        requests = []
        page.on('request', lambda request: requests.append(request.url) if request.resource_type == 'script' else None)
        page.goto(SITE.as_uri())
        self.assertTrue(any('demo.js?v=' in url for url in requests), requests)
        self.assertFalse(any(url.endswith('/demo.js') for url in requests), requests)
        self.assertTrue(page.get_by_role('button', name='Animation neu starten').is_visible())

    def test_story_reduced_motion_and_no_horizontal_overflow(self):
        for scheme in ('light', 'dark'):
            for width in (320, 390, 1280):
                with self.subTest(scheme=scheme, width=width):
                    page = self.browser.new_page(viewport={'width': width, 'height': 800}, color_scheme=scheme, reduced_motion='reduce')
                    self.addCleanup(page.close)
                    page.goto(SITE.as_uri())
                    self.assertEqual(page.locator('#story li').count(), 8)
                    self.assertTrue(page.locator('#paper-cross').is_visible())
                    self.assertTrue(page.locator('#story-done').is_visible())
                    self.assertFalse(page.get_by_role('button', name='Animation neu starten').is_visible())
                    self.assertFalse(page.locator('#story-stage').is_visible())
                    self.assertLessEqual(page.evaluate('document.documentElement.scrollWidth'), width)

    def test_story_player_mobile_and_desktop_scene_stays_inside_viewport(self):
        for scheme in ('light', 'dark'):
            for width in (320, 390, 1280):
                with self.subTest(scheme=scheme, width=width):
                    page = self.page(width, scheme)
                    page.clock.install()
                    page.get_by_role('button', name='Animation neu starten').click()
                    for frame in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
                        self.assertLessEqual(page.evaluate('document.documentElement.scrollWidth'), width)
                        self.assertEqual(page.locator('#story-art svg').count(), 1)
                        box = page.locator('#story-art svg').bounding_box()
                        self.assertGreaterEqual(box['x'], 0)
                        self.assertLessEqual(box['x'] + box['width'], width + 1)
                        if frame < 9:
                            page.clock.run_for(2400)

    def test_mobile_heading_uses_available_width_without_splitting_words(self):
        for width in (320, 360, 390, 545, 768):
            with self.subTest(width=width):
                page = self.page(width)
                dimensions = page.evaluate('''() => {
                    const h = document.querySelector('h1');
                    const range = document.createRange();
                    const walker = document.createTreeWalker(h, NodeFilter.SHOW_TEXT);
                    let split = [];
                    while (walker.nextNode()) {
                        const node = walker.currentNode;
                        for (const match of node.textContent.matchAll(/\\S+/g)) {
                            range.setStart(node, match.index);
                            range.setEnd(node, match.index + match[0].length);
                            if (range.getClientRects().length > 1) split.push(match[0]);
                        }
                    }
                    return {heading: h.getBoundingClientRect().width,
                            available: h.parentElement.getBoundingClientRect().width,
                            scroll: document.documentElement.scrollWidth, split};
                }''')
                self.assertGreaterEqual(dimensions['heading'], dimensions['available'] * 0.95)
                self.assertLessEqual(dimensions['scroll'], width)
                self.assertEqual(dimensions['split'], [])

    def test_theme_follows_system_and_readable_controls(self):
        for scheme in ('light', 'dark'):
            for width in (360, 1280):
                with self.subTest(scheme=scheme, width=width):
                    page = self.page(width, scheme)
                    self.assertEqual(page.evaluate('getComputedStyle(document.documentElement).colorScheme'), scheme)
                    page.locator('.technical-example summary').click()
                    page.get_by_label('Ziel auswählen').select_option('applicant')
                    page.get_by_role('button', name='Zuordnung bestätigen').click()
                    contrasts = page.evaluate('''() => {
                        const lum = rgb => {
                            const c = rgb.match(/\\d+(?:\\.\\d+)?/g).slice(0, 3).map(x => {
                                const s = Number(x)/255;
                                return s <= .04045 ? s/12.92 : ((s+.055)/1.055)**2.4;
                            });
                            return .2126*c[0]+.7152*c[1]+.0722*c[2];
                        };
                        const pairs = ['body', '.site-header .brand', '.nav a', '.hero-visual',
                          '.card p', '.pill', '.notice', '.field', 'select', '#confirm',
                          '#reset', '#result', '.month', '.status-box', '.foot a'];
                        return pairs.map(selector => {
                            const el = document.querySelector(selector);
                            const fg = getComputedStyle(el).color;
                            let bg = getComputedStyle(el).backgroundColor;
                            let ancestor = el;
                            while (bg === 'rgba(0, 0, 0, 0)' && ancestor.parentElement) {
                                ancestor = ancestor.parentElement;
                                bg = getComputedStyle(ancestor).backgroundColor;
                            }
                            const a = lum(fg), b = lum(bg);
                            return {selector, ratio:(Math.max(a,b)+.05)/(Math.min(a,b)+.05)};
                        });
                    }''')
                    for contrast in contrasts:
                        self.assertGreaterEqual(contrast['ratio'], 4.5, contrast['selector'])
                    self.assertLessEqual(page.evaluate('document.documentElement.scrollWidth'), width)

if __name__ == '__main__':
    unittest.main(verbosity=2)
