# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 22:58:40 2020

@author: Zixin
"""

import requests
import re
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.find_all('td', {'class': "posterColumn"}):
        print(post_text)
        imgLink = post_text.find_all('img') # class:resultSet
        print(imgLink)
        print(post_text[0].get('alt'))
        # content  = movieName.string
        # words = content.lower().split()  # lower all words and split them
        # for each_word in words:
        #     print(each_word)
        #     word_list.append(each_word)
            
start('https://www.imdb.com/chart/top?ref_=nv_ch_250_4')