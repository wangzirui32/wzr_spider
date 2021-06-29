import requests
from fake_useragent import UserAgent as UA

class Crawler():
    def __init__(self, url_list, parse_func, save_data_func, method="GET"):
        self.method = method
        self.url_list = url_list
        self.parse = parse_func
        self.save_data = save_data_func
        self.data = []
        self.headers = {
            "User-Agent": UA().random,
        }
    
    def request(self):
        try:
            self.headers = {
                "User-Agent": UA().random,
            }
            self.reponse = requests.request(self.method,
                                            self.url_list.get_url(),
                                            headers=self.headers)
        except Exception:
            return False
        else:
            return True

    def start_parsing(self):
        try:
            self.data.append(self.parse(self.reponse))
        except Exception:
            return False
        else:
            return True

    def start_crawling(self):
        while self.url_list.get_urls_size():
            self.request()
            self.start_parsing()
        self.save_data(self.data)