# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 23:46:41 2020

@author: Zixin
"""
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.finn.no/job/fulltime/search.html?page=' + str(page) + '&q=data'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for lnk in soup.find_all('a', {'class':"ads__unit__link"}):
            href = "https://www.finn.no" + lnk.get('href')
            print(href)
        page += 1

trade_spider(3)
            
