"""LIB to Sodexo."""
import enum
from html.parser import HTMLParser

def parse_html(html: str) -> str:
    result = html
    index = result.find('<div class="valor_saldo">')
    result = result[index:]
    index = result.find('</div>')
    result = result[0:index]

    parser = HtmlParser()
    parser.feed(result)

    return parser.data


class HtmlParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.data = []
        self.capture = False

    def handle_starttag(self, tag, attrs):
        if tag in ('div'):
            self.capture = True

    def handle_endtag(self, tag):
        if tag in ('div'):
            self.capture = False

    def handle_data(self, data):
        if self.capture:
            self.data.append(data)


class AccountDetails:
    """Represents an Account Details."""

    def __init__(self, amount: float, updated: str):
        self._amount = amount
        self._updated = updated
        
    @property
    def updated(self) -> str:
        return self._updated

    @property
    def amount(self) -> float:
        return self._amount
        