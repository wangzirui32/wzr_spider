# Wzr_Spider 爬虫框架
Wzr_Spider是一个简单的爬虫框架，使用它很简单。
首先，您需要创建一个网址列表，代码：
```py
from wzr_spider import *
url_list = UrlList(["https://github.com", "https://gitee.com"])
```
然后，编写解析HTML的函数：
```py
from bs4 import BeautifulSoup
def parse(reponse):
    """抓取每个页面的标题"""
    soup = BeautifulSoup(reponse.text, "html.parser")
    title = soup.find("title").get_text()
    return title
```
接着，编写处理数据的函数：
```py
def processing_data(data):
    with open("title.txt", "w", encoding="UTF-8") as f:
        f.write("\n".join(data))
```
最后，创建爬虫项目并开始运行：
```py
crawler = Crawler(url_list, parse, processing_data)
crawler.start_crawling()
```
运行结束后，打开目录下的title.txt，可以看到成功抓取数据。
```
GitHub: Where the world builds software · GitHub
Gitee | Software Development and Collaboration Platform
```