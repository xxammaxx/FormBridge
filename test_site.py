import os
from pathlib import Path
import unittest

from playwright.sync_api import sync_playwright

PAGE = Path(__file__).with_name("index.html").as_uri()


class Website(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = sync_playwright().start()
        cls.browser = cls.driver.chromium.launch(
            executable_path=os.environ.get("CHROMIUM_EXECUTABLE"),
            args=["--no-sandbox"],
        )

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.driver.stop()

    def test_documents_and_links(self):
        page = self.browser.new_page()
        self.addCleanup(page.close)
        page.goto(PAGE)
        self.assertEqual(page.locator("h1").count(), 1)
        self.assertEqual(page.locator("html").get_attribute("lang"), "de")
        ids = page.locator("[id]").evaluate_all("(els) => els.map(el => el.id)")
        self.assertEqual(len(ids), len(set(ids)))
        for link in page.locator('a[href^="#"]').all():
            self.assertIn(link.get_attribute("href")[1:], ids)
        for element in page.locator("script[src]").all():
            self.assertIn("?v=", element.get_attribute("src"))
        page.keyboard.press("Tab")
        self.assertEqual(page.locator(":focus").inner_text(), "Zum Inhalt")
        page.keyboard.press("Enter")
        self.assertTrue(page.url.endswith("#inhalt"))

    def test_responsive_themes_and_local_assets(self):
        for width in (320, 360, 390, 545, 768, 1280, 1920):
            for scheme in ("light", "dark"):
                with self.subTest(width=width, scheme=scheme):
                    page = self.browser.new_page(viewport={"width": width, "height": 850},
                                                 color_scheme=scheme)
                    try:
                        requests, errors = [], []
                        page.on("pageerror", lambda error: errors.append(str(error)))
                        page.on("requestfailed", lambda r: errors.append(r.url))
                        page.on("request", lambda r: requests.append(r.url))
                        page.goto(PAGE)
                        self.assertFalse(any(r.startswith(("http:", "https:")) for r in requests))
                        self.assertEqual(errors, [])
                        self.assertTrue(page.locator(".cover img").evaluate("img => img.naturalWidth > 0"))
                        self.assertEqual(page.evaluate("getComputedStyle(document.documentElement).colorScheme"), scheme)
                        self.assertLessEqual(page.evaluate("document.documentElement.scrollWidth"), width)
                        for el in page.locator("h1, h2, h3").all():
                            self.assertTrue(el.evaluate("el => el.scrollWidth <= el.clientWidth + 1"), el.inner_text())
                        split = page.locator("h1").evaluate("""el => {
                          const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
                          const range = document.createRange();
                          while (walker.nextNode()) {
                            for (const match of walker.currentNode.textContent.matchAll(/\\S+/g)) {
                              range.setStart(walker.currentNode, match.index);
                              range.setEnd(walker.currentNode, match.index + match[0].length);
                              if (range.getClientRects().length > 1) return true;
                            }
                          }
                          return false;
                        }""")
                        self.assertFalse(split)
                    finally:
                        page.close()


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(str(Path(__file__).parent), pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(not result.wasSuccessful())
