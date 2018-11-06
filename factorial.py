# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 01:02:26 2018

@author: Maltesh_Kumar
"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

n = int(input("Enter the number to find factorial = "))
print(fact(n))