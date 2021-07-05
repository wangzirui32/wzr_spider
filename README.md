# Wzr_Spider 爬虫框架
Wzr_Spider是一个简单的爬虫框架，使用它很简单。
本爬虫框架会自动检测网页的编码，将乱码编译成正常的字符串，
而且内置了爬虫线程，较多网址时可以开启5个线程同时抓取，
抓取时依赖于requests和lxml模块。
***
首先，您需要创建一个网址列表，代码：
```py
from wzr_spider import *
url_list = UrlList(["https://github.com", "https://gitee.com"])
```
然后，选择需要抓取的字段：
```py
"""
Item参数解释：
Xpath路径
Item名称
是否获取所有相关标签
"""
item_list = [Item("//title/text()", "title", False)]
```
接着，编写处理数据的函数：
```py
def processing_data(data):
    with open("title.txt", "w", encoding="UTF-8") as f:
        write_content = ""
        for i in data:
            write_content += i['title'] + "\n"
        f.write(write_content)
```
最后，创建爬虫项目并开始运行：
```py
crawler = Crawler(url_list, item_list, processing_data)
crawler.start_crawling()
```
运行结束后，打开目录下的title.txt，可以看到成功抓取数据。
```
GitHub: Where the world builds software · GitHub
Gitee | Software Development and Collaboration Platform
```
