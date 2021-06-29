import requests
from fake_useragent import UserAgent as UA

def request_page(method, url_list):
    headers = {
        "User-Agent": UA().random,
    }
    reponse = requests.request(method, url_list.get_url(), headers=headers)

    return reponse