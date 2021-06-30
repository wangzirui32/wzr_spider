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
    def __init__(self, url_list, parse_func, tag_list, method="GET"):
        super().__init__()
        self.parse = parse_func
        self.url_list = url_list
        self.tag_list = tag_list
        self.method = method

    def run(self):
        self.tag_data = []
        while self.url_list.get_urls_size():
            try:
                reponse = get_page(self.method, self.url_list)
                soup = BeautifulSoup(reponse.text, "lxml")
                temp_tag_data = []
                for i in self.tag_list:
                    tag = i.get_this_tag(soup)
                    temp_tag_data.append(tag)
                self.tag_data.append(temp_tag_data)
            except Exception:
                continue

def get_thread_tag_data(thread_list):
    all_data = []
    for t in thread_list:
        all_data += t.tag_data

    return all_data
