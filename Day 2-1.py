# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:07:40 2020

@author: USER
"""
import random
x=random.randint(1,20)
y=int(input("Guess the number"))

if y < 1 or y >10:
     print("Errow")
elif  x == y:
    print("You've got it")
else:
    print("guessed wrong")