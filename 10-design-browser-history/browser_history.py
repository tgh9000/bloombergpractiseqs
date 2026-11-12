import unittest


class BrowserHistory:
    def __init__(self, homepage):
        self.history = [homepage]
        self.current = 0

    def visit(self, url):
        self.history.append(url)
        self.current = len(self.history) - 1

    def back(self, steps):
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps):
        self.current = min(len(self.history), self.current + steps)
        return self.history[self.current]


class BrowserHistoryTests(unittest.TestCase):
    def test_back_returns_previous_page(self):
        browser = BrowserHistory("home.com")
        browser.visit("a.com")
        browser.visit("b.com")
        self.assertEqual(browser.back(1), "a.com")

    def test_back_stops_at_homepage(self):
        browser = BrowserHistory("home.com")
        browser.visit("a.com")
        self.assertEqual(browser.back(10), "home.com")

    def test_forward_after_back(self):
        browser = BrowserHistory("home.com")
        browser.visit("a.com")
        browser.back(1)
        self.assertEqual(browser.forward(1), "a.com")

    def test_forward_stops_at_latest_page(self):
        browser = BrowserHistory("home.com")
        browser.visit("a.com")
        browser.visit("b.com")
        browser.back(2)
        self.assertEqual(browser.forward(5), "b.com")

    def test_forward_past_end_raises(self):
        browser = BrowserHistory("home.com")
        browser.visit("a.com")
        with self.assertRaises(IndexError):
            browser.forward(1)


if __name__ == "__main__":
    unittest.main()
