import threading
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent as UA

def get_page(method, url_list):
    headers = {
        "User-Agent": UA().random,
    }
    reponse = requests.request(method, url_list.get_url(), headers=headers)

    return reponse

class CrawlerThread(threading.Thread):
    def __init__(self, url_list, parse_func, item_list, method="GET"):
        super().__init__()
        self.parse = parse_func
        self.url_list = url_list
        self.item_list = item_list
        self.method = method

    def run(self):
        self.item_data = []
        while self.url_list.get_urls_size():
            try:
                reponse = get_page(self.method, self.url_list)
                soup = BeautifulSoup(reponse.text, "lxml")

                for i in self.item_list:
                    tag_item_data = i.get_item_data(soup)
                    self.item_data.append(tag_item_data)
            except Exception:
                continue

def get_thread_item_data(thread_list):
    all_data = []
    for t in thread_list:
        all_data += t.item_data

    return all_data
