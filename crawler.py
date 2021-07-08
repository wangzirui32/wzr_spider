from .crawler_thread import *

class Crawler():
    def __init__(self, url_list,
                item_list=None,
                processing_data_func=None,
                thread_num=1,
                method="GET",
                request_params={}):
        self.url_list        = url_list
        self.item_list       = item_list
        self.processing_data = processing_data_func
        self.data            = []
        self.thread_num      = thread_num
        self.method          = method
        self.request_params  = request_params

    def __start_threading(self):
        self.thread_list = []
        for _ in range(self.thread_num):
            thread = CrawlerThread(self.url_list, self.item_list, self.method, self.request_params)
            thread.start()
            self.thread_list.append(thread)
        
        for t in self.thread_list:
            t.join()

    def start_crawling(self):
        self.__start_threading()
        self.data = get_thread_item_data(self.thread_list)
        if self.processing_data:
            self.processing_data(self.data)

    def get_crawler_data(self):
        return self.data