#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/4/22
# @file  获取知乎的图片.py
# description
"""
import urllib
from datetime import time
from typing import re

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.zhihu.com/question/29134042")
i = 0
while i < 10:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)
    try:
        driver.find_element_by_css_selector(
            'button.QuestionMainAction').click()
        print("page" + str(i))
        time.sleep(1)
    except:
        break
result_raw = driver.page_source
content_list = re.findall("img src=\"(.+?)\"", str(result_raw))
n = 0
while n < len(content_list):
    i = time.time()
    local = (r"%s.jpg" % (i))
    urllib.request.urlretrieve(content_list[n], local)
    print("编号：" + str(i))
    n = n + 1
