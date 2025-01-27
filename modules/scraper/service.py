from bs4 import BeautifulSoup
import requests


class ScaperService:
    def __init__(self, url: str = ""):
        self.url = url

    def curl(self, method: str = "get"):
        return requests.request(method, self.url)

    def parse_html(self, response: requests.Response):
        return BeautifulSoup(response.text, "html.parser")
