# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:44:47 2020

@author: USER
"""

import random
x=random.randint(1,20)
z=0
while True:
    z=z+1
    y=int(input("Guess the number"))
    if z == 5:
          print("you lose")
    elif y < 1 or y >20:
          print("Errow")
    elif  x == y:
          print("You've got it")
          w=int(z)
          print("How many times have you used?")
          print(w)
          print("time!!")
    else:
          print("guessed wrong")