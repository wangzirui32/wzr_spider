import threading
from lxml import etree
from .request import get_page

class CrawlerThread(threading.Thread):
    def __init__(self, url_list, item_list):
        super().__init__(daemon=True)
        self.url_list = url_list
        self.item_list = item_list

    def run(self):
        self.data = []
        while self.url_list.qsize():
            try:
                page = get_page("GET", self.url_list.get_url())
                if self.item_list:
                    html_obj = etree.HTML(page)

                    item_dict = {}
                    for i in self.item_list:
                        tag_item_data = i.get_item_data(html_obj)
                        item_dict.update(tag_item_data)

                    self.data.append(item_dict)
                else:
                    self.data.append(page)
            except Exception:
                continue

def get_thread_item_data(thread_list):
    all_data = []
    for t in thread_list:
        all_data += t.data

    return all_data
