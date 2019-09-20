# -*- coding: utf-8 -*-
"""
Spyder Editor
<<<<<<< HEAD
=======

>>>>>>> 45a9b9a3c0f23372da1f72f2e283325dffc7a1f6
This is a temporary script file.
"""
print('请输入你的名字')
playerName=input()
import random
print('输入任意值开始游戏')
goon=input()
gameTime=0
totalTime=0
minTime=1000
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

