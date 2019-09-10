# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:54:45 2019

@author: user
"""

import random
num=random.randint(1,100)
time=0
while True:
    guess=int(input("请猜一个1-100的数字："))
    if num < guess:
        print("猜大了，再试试")
        time += 1
    elif num > guess:
        print("猜小了，再试试")
        time += 1
    else:
        time +=1
        print("猜对了，你一共猜了%d轮" %time)
        break