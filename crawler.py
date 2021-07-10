from .crawler_thread import *

class Crawler():
    def __init__(self,
                url_list,
                item_list=None,
                processing_data_func=None,
                parse_func=None,
                thread_num=1,
                method="GET",
                request_params={},
                headers={},
                cookies="",
                output_message=True):
        self.url_list        = url_list
        self.item_list       = item_list
        self.parse           = parse_func
        self.processing_data = processing_data_func
        self.thread_num      = thread_num
        self.data            = []
        self.method          = method
        self.request_params  = request_params
        self.headers         = headers
        self.cookies         = cookies
        self.output_message  = output_message

    def __start_threading(self):
        self.thread_list = []
        for _ in range(self.thread_num):
            thread = CrawlerThread(self.url_list,
                                    self.item_list,
                                    self.method,
                                    self.parse,
                                    self.output_message,
                                    self.request_params,
                                    self.headers,
                                    self.cookies)
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