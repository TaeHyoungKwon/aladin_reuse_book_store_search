import json
import unittest
from unittest.mock import patch, Mock

from bs4 import BeautifulSoup

from constants import ALADIN_URL, BOOK_RESULT_HTML, BOOK_RESULT_TXT, INFO_MESSAGE
from crawling_aladin import crawl_aladin
from utils import is_korean, encode_euc_kr


class TestAladinCrawling(unittest.TestCase):
    @patch("crawling_aladin.convert_text_to_soup", Mock(return_value=BeautifulSoup("<html>None</html>", "html.parser")))
    @patch("crawling_aladin.request_get")
    def test_request_get_should_called_with_aladin_url_on_calling_aladin_url(self, mock_request_get):
        # When: Call crawl_aladin
        crawl_aladin()

        # Then: request_get should called with ALADIN_URL
        mock_request_get.assert_called_with(ALADIN_URL, None)

    @patch("crawling_aladin.convert_text_to_soup", Mock(return_value=BeautifulSoup("<html>None</html>", "html.parser")))
    @patch("crawling_aladin.request_get", Mock())
    def test_crawl_aladin_should_return_404_when_book_search_result_is_none(self):
        # When: Call crawl_aladin
        response = json.loads(crawl_aladin())

        # Then: should return 404 and NOT_FOUND
        self.assertEqual(response["status"], 404)
        self.assertEqual(response["message"], "NOT_FOUND")

    @patch("crawling_aladin.convert_text_to_soup", Mock(return_value=BeautifulSoup(BOOK_RESULT_HTML, "html.parser")))
    @patch("crawling_aladin.request_get", Mock())
    def test_crawl_aladin_should_return_200_when_book_search_result_is_exist(self):
        # When: Call crawl_aladin
        response = json.loads(crawl_aladin())

        # Then: should return 200 and OK
        self.assertEqual(response["status"], 200)
        self.assertEqual(response["message"], "OK")

    @patch("crawling_aladin.convert_text_to_soup", Mock(return_value=BeautifulSoup(BOOK_RESULT_HTML, "html.parser")))
    @patch("crawling_aladin.request_get", Mock())
    def test_crawl_aladin_should_return_book_result_txt_when_book_search_result_is_exist(self):
        # When: Call crawl_aladin
        response = json.loads(crawl_aladin())

        # Then: should return 200 and OK
        self.assertEqual(response["status"], 200)
        self.assertEqual(response["message"], "OK")
        # And: should return result message about book list
        self.assertEqual(response["result"], (INFO_MESSAGE
                                              + BOOK_RESULT_TXT.format(str(2))
                                              + "1. 할랄, 신이 허락한 음식만 먹는다 (반양장)\n"
                                              + "2. 문화코드, 어떻게 읽을 것인가 (반양장)"))

    def test_is_korean_should_return_true_when_given_text_is_korean(self):
        self.assertEqual(is_korean('한글123'), True)

    def test_is_korean_should_return_false_when_given_text_is_not_korean(self):
        self.assertEqual(is_korean('python123'), False)

    def test_encode_euc_kr_on_korean(self):
        self.assertEqual(encode_euc_kr('파이썬'), 'C6%C4%C0%CC%BD%E3')
