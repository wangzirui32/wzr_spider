import requests
from fake_useragent import UserAgent as UA

class Crawler():
    def __init__(self, url_list, parse_func, processing_data_func=None, method="GET"):
        self.method = method
        self.url_list = url_list
        self.parse = parse_func
        self.processing_data = processing_data_func
        self.data = []
    
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
        if self.processing_data:
            self.processing_data(self.data)