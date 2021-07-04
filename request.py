from chardet import detect
import requests
from fake_useragent import UserAgent as UA

def set_encoding(text):
    encode_mode = detect(text)['encoding']
    after_encoded = text.decode(encode_mode)

    return after_encoded

def get_page(method, url_list):
    headers = {
        "User-Agent": UA().random,
    }
    if url_list.get_urls_size():
        reponse = requests.request(method, url_list.get_url(), headers=headers)
        html = set_encoding(reponse.content)
        return html
    else:
        return None