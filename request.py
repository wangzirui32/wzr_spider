from chardet import detect
import requests
from fake_useragent import UserAgent as UA

def set_encoding(text):
    encode_mode = detect(text)['encoding']
    after_encoded = text.decode(encode_mode)

    return after_encoded

def get_page(method, url, request_params):
    headers = {
        "User-Agent": UA().random,
    }
    if method == 'GET':
        reponse = requests.request(method, url, headers=headers, params=request_params)
    else:
        reponse = requests.request(method, url, headers=headers, data=request_params)

    
    html = set_encoding(reponse.content)

    return html