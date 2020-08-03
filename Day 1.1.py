# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:58:23 2020

@author: USER
"""

x=input("What is your height\n")
y=input("What is your weight\n")
h=float(x)
w=float(y)
bmi=float(w//h**2)
if bmi <=18.5:
    print("太輕了")
elif bmi <=24:
    print("正常")
elif bmi <=27:
    print("過重")
elif bmi <=30:
    print("輕度肥胖")
elif bmi <=35:
    print("中度肥胖")
else:
    print("重度肥胖")