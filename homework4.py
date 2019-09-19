# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:50:11 2019

@author: user
"""
import random
print('输入任意值开始游戏')
goon=input()
while goon:
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
    print("是否继续游戏？（输入'y'继续，其他退出）")
    goon=bool('y'==input())
print('退出游戏，欢迎下次再来')     
        