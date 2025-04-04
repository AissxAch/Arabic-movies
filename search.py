import requests,urllib3
from info import *
from telebot import *
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def search1(a):
    s = a
    url = f"https://app.arabypros.com/api/search/{s}/0/4F5A9C3D9A86FA54EACEDDD635185/d506abfd-9fe2-4b71-b979-feff21bcad13/"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        'Accept-Encoding': "gzip",
        'Accept': "application/json",
        'Connection': "keep-alive",
        'Referer': "https://app.arabypros.com/",
    }
    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def search2(a):
    id = a
    url = f"https://app.arabypros.com/api/movie/source/by/{id}/4F5A9C3D9A86FA54EACEDDD635185/d506abfd-9fe2-4b71-b979-feff21bcad13/"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        'Accept-Encoding': "gzip",
        'Accept': "application/json",
        'Connection': "keep-alive",
        'Referer': "https://app.arabypros.com/",
        'if-modified-since': "Mon, 23 Dec 2024 21:42:48 GMT",
    }
    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
        
