"""Behavioral regression tests for the illustrated two-route film."""
import os
from pathlib import Path
import unittest
from playwright.sync_api import sync_playwright

SITE = Path(os.environ.get("FORMBRIDGE_TEST_HTML", Path(__file__).with_name("index.html"))).resolve()


class FilmTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = sync_playwright().start()
        executable = os.environ.get("CHROMIUM_EXECUTABLE")
        options = {"executable_path": executable} if executable else {}
        cls.browser = cls.engine.chromium.launch(args=["--no-sandbox"], **options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.engine.stop()

    def open(self, **options):
        page = self.browser.new_page(**options)
        self.addCleanup(page.close)
        page.clock.install()
        page.goto(SITE.as_uri())
        return page

    def test_play_pause_restart_and_finish(self):
        page = self.open()
        page.locator("#film-toggle").click()
        page.clock.run_for(2500)
        self.assertEqual(page.locator("#film-title").inner_text(), "Ausdrucken")
        page.locator("#film-toggle").click()
        progress = page.locator("#film-progress").evaluate("el => el.value")
        page.clock.run_for(4000)
        self.assertEqual(progress, page.locator("#film-progress").evaluate("el => el.value"))
        page.locator("#film-toggle").click()
        page.clock.run_for(2000)
        self.assertIn("unterschreiben", page.locator("#film-title").inner_text())
        page.locator("#film-restart").click()
        page.clock.run_for(11000)
        self.assertGreater(float(page.locator("#film-verdict").get_attribute("opacity")), .99)
        self.assertIn("Umweg", page.locator("#film-title").inner_text())
        page.clock.run_for(10000)
        self.assertEqual(page.locator("#film-toggle").inner_text(), "Erneut abspielen")
        self.assertIn("digital", page.locator("#film-title").inner_text())

    def test_signature_tracks_finger(self):
        page = self.open()
        page.locator("#film-toggle").click()
        page.clock.run_for(7 * 2000 + 1000)
        self.assertIn("Finger", page.locator("#film-title").inner_text())
        values = page.evaluate("""() => {
          const sig = document.querySelector('#film-signature');
          const part = 1 - Number(sig.style.strokeDashoffset);
          const path = document.querySelector('#film-signature-shape');
          const strokeTip = path.getPointAtLength(path.getTotalLength() * part).matrixTransform(sig.getCTM());
          const fingerTip = new DOMPoint().matrixTransform(document.querySelector('#film-finger').getCTM());
          return [part, Math.hypot(fingerTip.x - strokeTip.x, fingerTip.y - strokeTip.y)];
        }""")
        self.assertGreater(values[0], .01)
        self.assertLess(values[0], .99)
        self.assertLess(values[1], .5)

    def test_paper_to_phone_cut_matches_signature_anchor_and_real_scale(self):
        page = self.open()
        page.locator("#film-toggle").click()
        page.clock.run_for(11400)
        self.assertGreater(float(page.locator("#film-verdict").get_attribute("opacity")), .99)
        paper_anchor = page.locator("#film-paper").evaluate(
            "el => new DOMPoint().matrixTransform(el.getCTM()).toJSON()"
        )
        paper_width = page.locator("#film-paper use").first.bounding_box()["width"]
        page.clock.run_for(810)
        self.assertEqual(page.locator("#film-chapter").inner_text(), "Zukunftsvision · Digital")
        phone_anchor = page.locator("#film-mobile").evaluate(
            "el => new DOMPoint().matrixTransform(el.getCTM()).toJSON()"
        )
        self.assertAlmostEqual(paper_anchor["x"], phone_anchor["x"], places=2)
        self.assertAlmostEqual(paper_anchor["y"], phone_anchor["y"], places=2)
        phone_width = page.locator("#film-phone-body").bounding_box()["width"]
        self.assertLess(phone_width, paper_width * .5)
        page.clock.run_for(1800)
        zoomed_anchor = page.locator("#film-mobile").evaluate(
            "el => new DOMPoint().matrixTransform(el.getCTM()).toJSON()"
        )
        self.assertAlmostEqual(paper_anchor["x"], zoomed_anchor["x"], places=2)
        self.assertAlmostEqual(paper_anchor["y"], zoomed_anchor["y"], places=2)

    def test_reduced_motion_and_no_script_have_readable_routes(self):
        for options in ({"reduced_motion": "reduce"}, {"java_script_enabled": False}):
            with self.subTest(options=options):
                page = self.open(**options)
                self.assertTrue(page.locator(".film-static").is_visible())
                self.assertEqual(page.locator(".film-static li").count(), 8)
                self.assertFalse(page.locator(".film-player").is_visible())

    def test_player_fits_narrow_screen_in_both_modes(self):
        for mode in ("dark", "light"):
            with self.subTest(mode=mode):
                page = self.open(color_scheme=mode, viewport={"width":320, "height":707})
                for selector in ("#film-screen", "#film-toggle", "#film-restart", "#film-progress"):
                    box = page.locator(selector).bounding_box()
                    self.assertGreaterEqual(box["x"],0)
                    self.assertLessEqual(box["x"] + box["width"],320)


if __name__ == "__main__":
    unittest.main()
