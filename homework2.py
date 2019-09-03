# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:14:53 2019

@author: user
"""

num = 45
time = 0
while time < 3:
    guess=int(input('请输入一个数：'))
    if num > guess:
        print('你猜的数字是：',guess,',猜小了')
    elif num < guess:
        print('你猜的数字是：',guess,',猜大了')
    else:
        print ('你猜的数字是：',guess,',猜中了')
    time +=1
    