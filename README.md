# Wzr_Spider 爬虫框架
Wzr_Spider是一个简单的爬虫框架，使用它很简单。
首先，您需要创建一个网址列表，代码：
```py
from wzr_spider import *
url_list = UrlList(["https://github.com", "https://gitee.com"])
```
然后，选择需要抓取的字段：
```py
"""
Item参数解释：
爬取标签名称
标签属性
爬取属性内容
是否爬取所有相关标签
"""
item_list = [Item("title", {}, "title", "text", False)]
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
