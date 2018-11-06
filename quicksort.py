# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 16:02:18 2018

@author: Maltesh_Kumar
"""



def sort(a,low,high):
    p = 0
    if (high-low) > 0:
        p = quicksort(a,low,high)
        sort(a,low,p-1)
        sort(a,p+1,high) 


def quicksort(a,low,high): 
    pivot = high 
    i = low
    for j in range(low,high):
        if a[j] < a[pivot]:
            a[j],a[i] = a[i],a[j]
            i += 1
    a[i],a[pivot] = a[pivot],a[i]
    return i
        

n = int(input("Enter n = "))
a = input("Enter elements seperated by comma : ").split(",")
sort(a,0,len(a)-1)
print("Sorted elements :"," ".join(a))