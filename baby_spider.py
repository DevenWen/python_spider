#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   baby_spider.py
@Time    :   2020/07/30 00:57:28
@Author  :   kangqiang :)
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
import requests

if __name__ == "__main__":
    print('hello baby spider!')
    target = "https://www.baidu.com"
    req = requests.get(url=target)
    print(req.text)