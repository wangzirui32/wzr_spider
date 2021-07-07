# Wzr_Spider 爬虫框架
Wzr_Spider是一个简单的爬虫框架，使用它很简单。
本爬虫框架会自动检测网页的编码，将乱码编译成正常的字符串，
而且内置了爬虫线程，较多网址时可以开启多个线程同时抓取，
抓取时依赖于requests和lxml模块。
***
首先，您需要创建一个网址列表，代码：
```py
from wzr_spider import UrlList, Item, Crawler
url_list = UrlList(["https://blog.csdn.net", "https://www.baidu.com"])
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
# 注：thread_num代表开启的进程数，默认为1个
crawler = Crawler(url_list, item_list, processing_data, thread_num=1)
crawler.start_crawling()
```
运行结束后，打开目录下的title.txt，可以看到成功抓取数据。
```
CSDN博客 - 专业IT技术发表平台
百度一下，你就知道
```
提示：爬虫器返回的信息的结构如下：
```json
[{"item_1": "data_list_1", "item_2": "data_list_2" ...},
 {"item_1": "data_list_1", "item_2": "data_list_2" ...},
 ...
]
```
列表的第一项为第一个页面爬取的字段信息，第二项为第二个页面爬取的信息。
以此类推，列表的项数为URL的数量是相同的，每一项都是以字段名为键，数据为值的字典。
这样就完成了一整个爬虫的链条。

当然，如果你只想读取数据，Crawler类中的解析数据的函数（processing_data）可以不加，
要获取数据就要调用Crawler的方法get_crawler_data，它会返回爬虫器返回的字段数据。示例：
```py
from wzr_spider import UrlList, Item, Crawler
url_list = UrlList(["https://blog.csdn.net", "https://www.baidu.com"])
item_list = [Item("//title/text()", "title", False)]

crawler = Crawler(url_list, item_list, thread_num=1)
crawler.start_crawling()
print(crawler.get_crawler_data())
```
运行代码，输出：
```json
[{"title": "CSDN博客 - 专业IT技术发表平台"}, {"title": "百度一下，你就知道"}]
```
可以看到，get_crawler_data函数成功返回了爬取的数据。
还有，如果你想只获取页面，可以不加字段（item_list）参数，如下代码所示：
```py
from wzr_spider import UrlList, Crawler
# 这是一个API接口
url_list = UrlList(["https://api.github.com/"])

crawler = Crawler(url_list)
crawler.start_crawling()
print(crawler.get_crawler_data())
```
输出：
```js
['{\n  "current_user_url": "https://api.github.com/user",\n  "current_user_authorizations_html_url": "https://github.com/settings/connections/applications{/client_id}",\n ...
']
```
接下来，可以使用json模块进行处理，转化为json格式数据并保存：
```py
print(crawler.get_crawler_data())

# 新增代码
import json
data = json.loads(crawler.get_crawler_data().replace("\n", ""))
f = open("data.json", "w")
json.dumps(f)
f.close()
```
运行代码，查看data.json文件：
```json
{"current_user_url": "https://api.github.com/user", "current_user_authorizations_html_url": "", ...}
```
由于页面上的json数据参杂了很多“\n”换行符，所以要去掉换行符再进行转换。