#!/usr/bin/env python3.6
#coding=utf-8
#��ŵ������
B=[]
def move(n,a,b,c):
	if n == 1:
		buzhou = a + str(n) + '-->' + c + str(n)
		B.append(buzhou)
		return
	else:
		move(n-1,a,c,b)#n-1�����Ӵ�a-b
		move(1,a,b,c)#1�����Ӵ�a-c
		move(n-1,b,a,c)#n-1�����Ӵ�b-c
move(3,'A','B','C')
print(B)
