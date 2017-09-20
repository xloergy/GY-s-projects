# coding: utf-8

import requests

# bautifulsoup

url = 'http://d1.weather.com.cn/calendar_new/2017/101020100_201709.html?_=1504768868459'
r = requests.get(url)

print(r.content.decode('utf8'))