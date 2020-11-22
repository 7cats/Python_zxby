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
        for link in soup.find_all('a', {'class':"ads__unit__link"}):
            href = "https://www.finn.no" + link.get('href')
            # get the title
            title = link.string
            print(href)
            print(title)
            get_single_item_data(href) 
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('font', {'style':'vertical-align: inherit;'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = str("https://www.finn.no") + str(link.get('href'))
        print(href)
        
trade_spider(1)
    
