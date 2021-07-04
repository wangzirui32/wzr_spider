import threading
from bs4 import BeautifulSoup
from .request import get_page

class CrawlerThread(threading.Thread):
    def __init__(self, url_list, item_list, method="GET"):
        super().__init__()
        self.url_list = url_list
        self.item_list = item_list
        self.method = method

    def run(self):
        self.item_data = []
        while self.url_list.get_urls_size():
            try:
                html = get_page(self.method, self.url_list)
                soup = BeautifulSoup(html, "lxml")

                item_dict = {}
                for i in self.item_list:
                    tag_item_data = i.get_item_data(soup)
                    item_dict.update(tag_item_data)

                self.item_data.append(item_dict)
            except Exception:
                continue

def get_thread_item_data(thread_list):
    all_data = []
    for t in thread_list:
        all_data += t.item_data

    return all_data
