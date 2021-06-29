from .crawler_thread import *

class Crawler():
    def __init__(self, url_list, parse_func, processing_data_func=None, method="GET"):
        self.method = method
        self.url_list = url_list
        self.parse = parse_func
        self.processing_data = processing_data_func
        self.data = []

    def start_crawling(self):
        thread_num = 1
        if self.url_list.get_urls_size() > 5:
            thread_num = 5

        self.thread_list = []
        for i in range(thread_num):
            thread = CrawlerThread(self.url_list, self.parse, self.method)
            thread.start()
            self.thread_list.append(thread)
        
        for t in self.thread_list:
            t.join()
        
        for i in self.thread_list:
            self.data += i.data

        if self.processing_data:
            self.processing_data(self.data)
