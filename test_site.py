import pathlib
import unittest
from playwright.sync_api import sync_playwright

SITE = pathlib.Path(__file__).with_name('index.html')

class SiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p = sync_playwright().start()
        cls.browser = cls.p.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox'])

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.p.stop()

    def page(self, width=1280):
        page = self.browser.new_page(viewport={'width': width, 'height': 800})
        self.addCleanup(page.close)
        page.goto(SITE.as_uri())
        return page

    def test_navigation_and_research_status(self):
        page = self.page()
        self.assertEqual(page.locator('main section').count(), 6)
        self.assertIn('Forschungsprojekt', page.locator('h1').inner_text())
        self.assertIn('Simulation', page.locator('#demo').inner_text())
        self.assertIn('keine fertige', page.locator('#forschung').inner_text())
        for link in page.locator('nav a[href^="#"]').all():
            self.assertEqual(page.locator(link.get_attribute('href')).count(), 1)

    def test_mapping_requires_human_confirmation(self):
        page = self.page()
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
        page.get_by_label('Ziel auswählen').select_option('unknown')
        page.get_by_role('button', name='Zuordnung bestätigen').click()
        self.assertIn('Keine Zuordnung', page.locator('#result').inner_text())
        self.assertNotIn('Alex Muster', page.locator('#result').inner_text())

    def test_conflicting_section_does_not_export_value(self):
        page = self.page()
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

if __name__ == '__main__':
    unittest.main(verbosity=2)
