from chardet import detect
import requests
from fake_useragent import UserAgent as UA

def set_encoding(text):
    encode_mode = detect(text)['encoding']
    after_encoded = text.decode(encode_mode)

    return after_encoded

def get_page(method, url):
    headers = {
        "User-Agent": UA().random,
    }
    reponse = requests.request(method, url, headers=headers)
    html = set_encoding(reponse.content)

    return html