import threading
from lxml import etree
from .request import get_page

class CrawlerThread(threading.Thread):
    def __init__(self, url_list, item_list, method, request_params):
        super().__init__(daemon=True)
        self.url_list       = url_list
        self.item_list      = item_list
        self.method         = method
        self.request_params = request_params

    def run(self):
        self.data = []
        while self.url_list.qsize():
            try:
                page = get_page(self.method, self.url_list.get_url(), self.request_params)
                if self.item_list:
                    html_obj = etree.HTML(page)

                    item = {}
                    for i in self.item_list:
                        item_data = i.get_item_data(html_obj)
                        item.update(item_data)

                    self.data.append(item_data)
                else:
                    self.data.append(page)
            except Exception:
                continue

def get_thread_item_data(thread_list):
    all_data = []
    for t in thread_list:
        all_data += t.data

    return all_data
