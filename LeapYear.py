# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:35:05 2021

@author: Vishesh
"""
import datetime
import random
year = random.randint(1993,2018)
print(year)
if(year%4==0 and year%100!=0 or year%400==0):
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")
    