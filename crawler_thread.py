import threading
from lxml import etree
from .request import get_page
import colorama

colorama.init(autoreset=True)

class CrawlerThread(threading.Thread):
    def __init__(self,
                url_list,
                item_list,
                method,
                parse,
                output_message,
                request_params,
                headers,
                cookies):
        super().__init__()
        self.url_list       = url_list
        self.item_list      = item_list
        self.method         = method
        self.parse          = parse
        self.output_message = output_message
        self.request_params = request_params
        self.headers        = headers
        self.cookies        = cookies

    def run(self):
        self.data = []
        while self.url_list.qsize():
            try:
                url = self.url_list.get_url()
                page = get_page(self.method,
                                url,
                                self.request_params,
                                self.headers,
                                self.cookies)
                data = None
            
                if self.item_list:
                    html_obj = etree.HTML(page)

                    data = {}
                    for i in self.item_list:
                        item_data = i.get_item_data(html_obj)
                        data.update(item_data)
                elif self.parse:
                    data = self.parse(page)
                else:
                    data = page
                
                self.data.append(data)
            except Exception as e:
                if self.output_message: print('{}[ERROR] {} reports error "{}" on "{}" !'.format(colorama.Fore.YELLOW, self.name, e, url))
            else:
                if self.output_message: print('{}[INFO] {} crawled successfully at "{}" !'.format(colorama.Fore.LIGHTGREEN_EX, self.name, url))
        if self.output_message: print("{}[INFO] {} is over !".format(colorama.Fore.LIGHTGREEN_EX, self.name))

def get_thread_item_data(thread_list):
    all_data = []
    for t in thread_list:
        all_data += t.data

    return all_data
