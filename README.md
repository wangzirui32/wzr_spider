# Wzr_Spider 爬虫框架
Wzr_Spider是一个简单的爬虫框架，使用它很简单。
本爬虫框架会自动检测网页的编码，将乱码编译成正常的字符串，
而且内置了爬虫线程，较多网址时可以开启多个线程同时抓取，
抓取时依赖于requests和lxml模块。
***
# 1. Crawler对象参数
```py
Crawler(
    url_list,                    # 网址列表对象
    item_list=None,              # 字段对象列表
    processing_data_func=None,   # 处理数据的函数
    parse_func=None              # 网页解析函数
    thread_num=1,                # 爬取时开启的线程数
    method="GET",                # 爬取时使用的请求方式
    request_params={},           # 请求的参数或表单
    headers={},                  # 自定义请求头
    cookies="",                  # 自定义cookies
    output_message=True          # 是否输出提示信息
)
```
# 2. UrlList对象参数
```py
UrlList(urls)
```
urls为网址列表，如：
```py
UrlList(['http://url-1.com', 'http://url-2.com', ...])
```
# 3. Item对象参数
```py
Item(
    tag_xpath,         # 需要爬取标签的XPath
    item_name,         # 字段名称
    get_all_tag=False, # 是否获取所有相关标签
    default=None       # 爬取失败的填充值
)
```
# 4. 爬虫器数据结构
提示：爬虫器返回的信息的结构如下：
```js
[{"item_1": "data_list_1", "item_2": "data_list_2" ...},
 {"item_1": "data_list_1", "item_2": "data_list_2" ...},
 ...
]
```
列表的第一项为第一个页面爬取的字段信息，第二项为第二个页面爬取的信息。
以此类推，列表的项数为URL的数量是相同的，每一项都是以字段名为键，数据为值的字典。
当然，如果你加上了解析器函数，那么结构应该如下：
```
[目标网页1解析器返回数据, 目标网页2解析器返回数据, 目标网页3解析器返回数据, ...]
```
# 5. 基本示例
代码：
```py
from wzr_spider import UrlList, Item, Crawler

# 网址列表
url_list = UrlList(["https://blog.csdn.net", "https://www.baidu.com"])
# 字段列表
item_list = [Item("//title/text()", "title", False)]

# 处理数据函数
def processing_data(data):
    with open("title.txt", "w", encoding="UTF-8") as f:
        write_content = ""
        for i in data:
            write_content += i['title'] + "\n"
        f.write(write_content)

# 创建爬虫器对象
crawler = Crawler(url_list, item_list, processing_data, thread_num=1)
crawler.start_crawling()
```
运行结束后，打开目录下的title.txt，可以看到成功抓取数据。
```
CSDN博客 - 专业IT技术发表平台
百度一下，你就知道
```
当然，可以加上解析器函数：
```py
from wzr_spider import UrlList, Item, Crawler
from lxml import etree

url_list = UrlList(['https://blog.csdn.net/', "https://www.baidu.com"])

def parse(html):
    title = etree.HTML(html).xpath("//title/text()")[0]
    return title

crawler = Crawler(url_list, parse_func=parse)
crawler.start_crawling()
```
# 6. get_crawler_data方法
如果你只想读取数据，Crawler类中的解析数据的函数（processing_data）可以不加，
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
# 7. 只获取页面
如果你想只获取页面，可以不加字段（item_list）参数，为JSON接口的爬取提供了便利，如下代码所示：
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