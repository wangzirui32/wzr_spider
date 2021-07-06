from .crawler_thread import *

class Crawler():
    def __init__(self, url_list, item_list, processing_data_func=None, method="GET", thread_num=1):
        self.method          = method
        self.url_list        = url_list
        self.item_list       = item_list
        self.processing_data = processing_data_func
        self.data            = []
        self.thread_num      = thread_num

    def __start_threading(self):
        self.thread_list = []
        for _ in range(self.thread_num):
            thread = CrawlerThread(self.url_list, self.item_list, self.method)
            thread.start()
            self.thread_list.append(thread)
        
        for t in self.thread_list:
            t.join()

    def start_crawling(self):
        self.__start_threading()
        self.item_data = get_thread_item_data(self.thread_list)
        if self.processing_data:
            self.processing_data(self.item_data)

    def get_crawler_data(self):
        return self.item_data