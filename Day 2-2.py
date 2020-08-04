# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:21:18 2020

@author: USER
"""

import random
x=random.randint(1,20)
z=0
while True:
    y=int(input("Guess the number"))
    if y < 1 or y >20:
          print("Errow")
    elif  x != y:
          print("guessed wrong")
    else:
          print("You've got it")
          break