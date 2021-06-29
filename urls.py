import queue

class UrlList():
    def __init__(self, urls):
        self.url_list = queue.Queue(len(urls))

        for url in urls:
            self.url_list.put(url)

    def get_url(self):
        if self.url_list.qsize():
            return self.url_list.get()
        else:
            return None

    def get_urls_size(self):
        return self.url_list.qsize()