# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:21:53 2020

@author: USER
"""
e = int(input("What is your english score\n"))
m = int(input("What is your math  score\n"))
if e <= 90 and m >= 90:
    print("Have prizes")
elif e <=60 and m <=60:
    print("To be punished")
else:
    print("Refueling")