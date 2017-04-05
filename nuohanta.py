#!/usr/bin/env python3.6
#coding=utf-8
#汉诺塔方法
B=[]
def move(n,a,b,c):
	if n == 1:
		buzhou = a + str(n) + '-->' + c + str(n)
		B.append(buzhou)
		return
	else:
		move(n-1,a,c,b)#n-1个盘子从a-b
		move(1,a,b,c)#1个盘子从a-c
		move(n-1,b,a,c)#n-1个盘子从b-c
move(3,'A','B','C')
print(B)
