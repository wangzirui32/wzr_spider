from queue import Queue

class UrlList(Queue):
    def __init__(self, urls):
        super().__init__()
        for url in urls:
            self.put(url)

    def get_url(self):
        if self.qsize() != 0:
            return self.get()
        else:
            return None
