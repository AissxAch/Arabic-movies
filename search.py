import requests,urllib3
from info import *
from telebot import *
import re
def search1(a):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    s=a
    url = f"https://app.arabypros.com/api/search/{s}/0/4F5A9C3D9A86FA54EACEDDD635185/d506abfd-9fe2-4b71-b979-feff21bcad13/"
    headers = {'User-Agent': "okhttp/4.8.0",'Accept-Encoding': "gzip"}
    proxies = {
        "http": "http://c6qkybz1kv4wojl-country-dz:3v9ou724vjdpgdw@rp.proxyscrape.com:6060",
    }
    res = requests.get(url, headers=headers, proxies=proxies, verify=False).json()
    return res
    
def search2(a):
    id=a
    url = f"https://app.arabypros.com/api/movie/source/by/{id}/4F5A9C3D9A86FA54EACEDDD635185/d506abfd-9fe2-4b71-b979-feff21bcad13/"
    headers = {'User-Agent': "okhttp/4.8.0",'Accept-Encoding': "gzip",'if-modified-since': "Mon, 23 Dec 2024 21:42:48 GMT"}
    res2 = requests.get(url, headers=headers,verify=False).json()
    return res2
    # for l in res2:
    #     print(f'[+] [ Link : {l['url']} ]')