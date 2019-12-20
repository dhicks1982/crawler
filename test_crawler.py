import unittest
import crawler


class CrawlerTest(unittest.TestCase):
    def test_get_links_from_text(self):
        text = '<html><a href="http://abc.com">link</a><a href="https://cdf.com"</a><a href="http:/invalid"</a></html>'
        results = crawler.get_links_from_text(text)
        self.assertListEqual(["http://abc.com", "https://cdf.com"], results)

    def test_get_links_from_url(self):
        results = crawler.get_links_from_url("https://www.google.com")
        self.assertGreater(len(results), 3)


if __name__ == '__main__':
    unittest.main()