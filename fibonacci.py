# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 01:03:55 2018

@author: Maltesh_Kumar
"""

# Fibonacci Using Recursion
def fib(n):
    if n ==0:
        return 0 
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return(fib(n-1) + fib(n-2))

# res is used to calculate the sum of n values of fibonacci series 
res = 0        
n = int(input("Enter n = "))
for i in range(n):
    res = res + fib(i)
    print(fib(i),end=" ")
print()
print("The sum of numbers is = ",res)


########################################################

# Fibonacci Using FOR Loop
res = 0
n = int(input("Enter n = "))
first = 0
sec = 1
for i in range(n):
    res = res + first
    print(first,end=" ")
    temp = first
    first = sec
    sec = temp + sec
print()
print("The sum of numbers is = ",res)










    