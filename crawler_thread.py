import threading
import requests
from fake_useragent import UserAgent as UA

def get_page(method, url_list):
    headers = {
        "User-Agent": UA().random,
    }
    reponse = requests.request(method, url_list.get_url(), headers=headers)

    return reponse

class CrawlerThread(threading.Thread):
    def __init__(self, url_list, parse_func, method="GET"):
        super().__init__()
        self.parse = parse_func
        self.url_list = url_list
        self.method = method

    def run(self):
        self.data = []
        while self.url_list.get_urls_size():
            try:
                reponse = get_page(self.method, self.url_list)
                self.data.append(self.parse(reponse))
            except Exception:
                continue

def get_thread_data(thread_list):
    all_data = []
    for t in thread_list:
        all_data += t.data
    
    return all_data
