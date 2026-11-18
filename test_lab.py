import json
import os
import pathlib
import unittest

from playwright.sync_api import sync_playwright


class LabTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runtime = sync_playwright().start()
        cls.browser = cls.runtime.chromium.launch(
            executable_path=os.environ.get("CHROMIUM_EXECUTABLE"),
            args=["--no-sandbox"],
        )

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.runtime.stop()

    def setUp(self):
        self.page = self.browser.new_page(viewport={"width": 320, "height": 800})
        self.addCleanup(self.page.close)
        self.page.goto(os.environ.get("FORMBRIDGE_TEST_URL") or
                       pathlib.Path(__file__).with_name("index.html").as_uri())
        self.source = self.page.get_by_label("Formularausschnitt", exact=True)
        self.target = self.page.get_by_label("Ziel auswählen", exact=True)
        self.confirm = self.page.get_by_role("button", name="Zuordnung bestätigen")
        self.record = self.page.locator("#lab-output")

    def test_confirmation_and_changed_source(self):
        self.assertTrue(self.confirm.is_disabled())
        for context, name in [("applicant", "Muster"), ("household", "Beispiel")]:
            self.source.select_option(context)
            self.assertTrue(self.confirm.is_disabled())
            self.assertEqual(self.record.text_content(), "")
            self.target.select_option(context)
            self.assertTrue(self.record.is_hidden())
            self.confirm.focus()
            self.page.keyboard.press("Enter")
            self.assertEqual(json.loads(self.record.inner_text())["familienname"], name)
        self.page.locator("#reset").click()
        self.assertEqual(self.source.input_value(), "applicant")
        self.assertTrue(self.confirm.is_disabled())
        self.assertEqual(self.record.text_content(), "")
        self.assertTrue(self.source.evaluate("(el) => el === document.activeElement"))

    def test_changing_confirmed_target_revokes_output(self):
        self.target.select_option("applicant")
        self.confirm.click()
        self.assertTrue(self.record.is_visible())
        for choice, message in [("household", "Widerspruch"), ("unknown", "Keine Zuordnung")]:
            self.target.select_option(choice)
            self.assertTrue(self.record.is_hidden())
            self.confirm.click()
            self.assertIn(message, self.page.locator("#result").inner_text())
            self.assertEqual(self.record.text_content(), "")

    def test_missing_context_blocks_even_explicit_selection(self):
        self.source.select_option("ambiguous")
        for target in ["applicant", "household", "unknown"]:
            self.target.select_option(target)
            self.confirm.click()
            self.assertTrue(self.record.is_hidden())
            self.assertIn("offen", self.page.locator("#result").inner_text())


if __name__ == "__main__":
    unittest.main()
