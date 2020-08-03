# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:29:17 2020

@author: USER
"""

x=input("Enter grade\n")
y=int(x)
if y > 100 or y < 0:
  print("Errow")
elif y == 100:
    print("A+")
elif y >= 90:
    print("A")
elif y >= 80:
    print("B")
elif y >= 70:
    print("C")
elif y >= 60:
    print("D")
else:
    print("E")
    