# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:29:21 2017
功能：抓出小说内容
输入：网址 URL
输出：小说内容
@author: zr
"""

from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url = target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_ = 'showtxt')
    print(texts[0].text.replace('\xa0'*8,'\n\n'))      
    ''' 上述格式的转变很重要，包括正则表达式'''