#!/usr/bin/python
# -*- coding: utf-8 -*- 

# File name: crawler_location.py
# Author: Zhaowei Tan
# Contact: tanzw94@gmail.com

import urllib2

keyword = "复旦"
# initial_page = "http://www.haodf.com/jibing/keluoenbing_yiyuan_all_all_all_all_1.htm"
initial_page = "https://restapi.amap.com/v3/place/text?s=rsv3&children=&key=8325164e247e15eea68b59e89200988b&page=1&offset=10&city=110000&language=zh_cn&callback=jsonp_297495_&platform=JS&logversion=2.0&sdkversion=1.3&appname=https%3A%2F%2Flbs.amap.com%2Fconsole%2Fshow%2Fpicker&csid=C7061C68-7F93-49D2-AD38-5AA456956A1A&keywords=" + keyword
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
f = opener.open(initial_page)
content = f.read()

a = content.find("name")
b = content.find("\",", a)
print content[a+7:b]

a = content.find("address")
b = content.find("\",", a)
print content[a+10:b]

a = content.find("location")
b = content.find("\",", a)
print content[a+11:b]