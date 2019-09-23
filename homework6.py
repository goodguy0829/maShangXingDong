# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:12:04 2019

@author: user
"""

f=open('recordfile.txt')
recordfile=f.read()
f.close()
record=recordfile.split()
print('%s,你已经完玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案，开始游戏' %(record[0],int(record[3]),int(record[2]),int(record[1])/int(record[3])))
playerName=record[0]
import random
print('输入任意值开始游戏')
goon=input()
gameTime=int(record[3])
totalTime=int(record[1])
minTime=int(record[2])
while goon:
    num=random.randint(1,100)
    gameTime += 1
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
            totalTime += time
            averageTime = float(totalTime)/(float(gameTime))
            minTime=min(minTime,time)
            print('%s,你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案'%(playerName,gameTime,minTime,averageTime))
            break       
    print("是否继续游戏？（输入'y'继续，其他退出）")
    goon=bool('y'==input())
print('退出游戏，欢迎下次再来')  
recordfile='%s %d %d %d' %(playerName,totalTime,minTime,gameTime)
f=open('recordfile.txt','w')
f.write(recordfile)
f.close()