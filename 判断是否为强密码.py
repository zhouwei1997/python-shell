#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/6/8
# @file  判断是否为强密码.py
# description 使用input输入一个字符串，判断是否为强密码，长度至少8位，包含大写字母、小写字母、数字和下划线的则为强密码
"""

str = input("input you password:")
flag1, flag2, flag3, flag4 = True, True, True, True

if len(str) < 8:
    print("not enough length")
    exit();
else:
    count = 0
    for i in str:
        if i in "0123456789":
            if flag1:
                count += 1
                print("count1: {}".format(count))
                flag1 = False
        if i in "abcdefghigklmnopqrstuvwxyz":
            if flag2:
                count += 1
                print("count2: {}".format(count))
                flag2 = False
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if flag3:
                count += 1
                print("count3: {}".format(count))
                flag3 = False
        if i in "_":
            if flag4:
                count += 1
                print("count4: {}".format(count))
                flag4 = False
    if count == 4:
        print(str, " is strong password")
    else:
        print(str, " is not strong password")
