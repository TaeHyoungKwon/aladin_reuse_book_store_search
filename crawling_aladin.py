import json
import sys

import requests
from bs4 import BeautifulSoup

from constants import ALADIN_URL, USER_AGENT, BOOK_RESULT_TXT, EMPTY_SPACE, NEW_LINE, INFO_MESSAGE
from utils import encode_euc_kr, is_korean


def request_get(url, search_word):
    if is_korean(search_word):
        search_word = encode_euc_kr(search_word)

    return requests.get(url.format(search_word), headers={"USER-AGENT": USER_AGENT})


def convert_text_to_soup(response):
    return BeautifulSoup(response.text, "html.parser")


def crawl_aladin(search_word=None):
    def _searched_books():
        html = convert_text_to_soup(response)
        return html.find("div", {"id": "Search3_Result"})

    def _make_book_result_message(index, book):
        return "{number}. {book_title}".format(
            number=str(index), book_title=" ".join(book.text.replace(NEW_LINE, EMPTY_SPACE).split())
        )

    response = request_get(ALADIN_URL, search_word)

    if not _searched_books():
        return json.dumps({"status": 404, "message": "NOT_FOUND"})

    books = _searched_books().find_all("b", {"class": "bo3"})
    book_titles = NEW_LINE.join(_make_book_result_message(index, book) for index, book in enumerate(books, 1))

    return json.dumps(
        {"status": 200, "message": "OK", "result": INFO_MESSAGE + BOOK_RESULT_TXT.format(str(len(books))) + book_titles}
    )


if __name__ == "__main__":
    result = json.loads(crawl_aladin(sys.argv[1]))
    try:
        print(result["result"])
    except KeyError:
        print("찾으려는 책이 없습니다.")
