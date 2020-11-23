# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 22:58:40 2020

@author: Zixin
"""

import requests
import re
from bs4 import BeautifulSoup
import operator
import string

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.find_all('td', {'class': "posterColumn"}):
        # print(post_text)
        # imgLink = post_text.find_all('img') # class:resultSet
        # print(imgLink)
        # print(post_text[0].get('alt'))
        for post_text2 in post_text.find_all('img'):
            content = post_text2.get('alt')
            print(content)
        # content  = content.string
        words = content.lower().split()  # lower all words and split them
        for each_word in words:
            # print(each_word)
            word_list.append(each_word)
        clean_up_list(word_list)
            

# p = re.compile('[a-z]+')

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        # symbols = '[[:lower:]]'\
        # symbols = re.compile('[a-z]+')
        symbols = string.punctuation
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i],'')
        if len(word) > 0:
            # print(word)
            clean_word_list.append(word)
    create_dic(clean_word_list)

def create_dic(clean_word_list):
    word_list = {}
    for word in clean_word_list:
        if word in word_list:
            word_list[word]+=1
        else:
            word_list[word] =1
    for key, value in sorted(word_list.items(), key=operator.itemgetter(1)):
        print(key, value)



start('https://www.imdb.com/chart/top?ref_=nv_ch_250_4')


t = string.ascii_lowercase