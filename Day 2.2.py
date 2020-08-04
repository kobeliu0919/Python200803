# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:44:47 2020
3
@author: USER
"""
x=0
y=2
n = int(input("請輸入一個正整數:"))
while n>1 :
    if (n-y)>=1:
        if (n%y)>0:
            x=x+0
        else:
            x=x+1
        y=y+1
    else:
        break
if n == 1:
    print("不是質數")
elif x > 0:
    print("不是質數")
else:
    print("是質數")
    
    