from .crawler_thread import *

class Crawler():
    def __init__(self, url_list, item_list, processing_data_func, method="GET"):
        self.method = method
        self.url_list = url_list
        self.item_list = item_list
        self.processing_data = processing_data_func
        self.data = []

    def start_crawling(self):
        thread_num = 1
        if self.url_list.qsize() > 4:
            thread_num = 5

        self.thread_list = []
        for _ in range(thread_num):
            thread = CrawlerThread(self.url_list, self.item_list, self.method)
            thread.start()
            self.thread_list.append(thread)
        
        for t in self.thread_list:
            t.join()

        self.item_data = get_thread_item_data(self.thread_list)
        self.processing_data(self.item_data)
