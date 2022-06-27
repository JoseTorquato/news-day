import requests


class Requester: 
    def __init__(self, url) -> None:
        self.url = url
        self.headers = {
                    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
                }
        self.__requests = requests

    def get_web_page(self):
        return self.__requests.get(
                self.url,
                headers=self.headers
            )
