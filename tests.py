import json
import unittest
from unittest.mock import patch, Mock

from bs4 import BeautifulSoup

from constants import ALADIN_URL, BOOK_RESULT_HTML, BOOK_RESULT_TXT
from crawling_aladin import crawl_aladin


class TestAladinCrawling(unittest.TestCase):
    @patch("crawling_aladin.convert_text_to_soup", Mock(return_value=BeautifulSoup("<html>None</html>", "html.parser")))
    @patch("crawling_aladin.request_get")
    def test_request_get_should_called_with_aladin_url_on_calling_aladin_url(self, mock_request_get):
        crawl_aladin()
        mock_request_get.assert_called_with(ALADIN_URL, None)

    @patch("crawling_aladin.convert_text_to_soup", Mock(return_value=BeautifulSoup("<html>None</html>", "html.parser")))
    @patch("crawling_aladin.request_get", Mock())
    def test_crawl_aladin_should_return_404_when_book_search_result_is_none(self):
        response = json.loads(crawl_aladin())

        self.assertEqual(response["status"], 404)
        self.assertEqual(response["message"], "NOT_FOUND")

    @patch("crawling_aladin.convert_text_to_soup", Mock(return_value=BeautifulSoup(BOOK_RESULT_HTML, "html.parser")))
    @patch("crawling_aladin.request_get", Mock())
    def test_crawl_aladin_should_return_200_when_book_search_result_is_exist(self):
        response = json.loads(crawl_aladin())

        self.assertEqual(response["status"], 200)
        self.assertEqual(response["message"], "OK")

    @patch("crawling_aladin.convert_text_to_soup", Mock(return_value=BeautifulSoup(BOOK_RESULT_HTML, "html.parser")))
    @patch("crawling_aladin.request_get", Mock())
    def test_crawl_aladin_should_return_book_result_txt_when_book_search_result_is_exist(self):
        response = json.loads(crawl_aladin())

        self.assertEqual(response["status"], 200)
        self.assertEqual(response["message"], "OK")

        self.assertEqual(response["result"], (BOOK_RESULT_TXT.format(str(2))
                                              + "1. 할랄, 신이 허락한 음식만 먹는다 (반양장)\n"
                                              + "2. 문화코드, 어떻게 읽을 것인가 (반양장)"))
