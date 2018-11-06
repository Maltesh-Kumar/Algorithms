# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 00:51:17 2018

@author: Maltesh_Kumar
"""

n = int(input("Enter dimension n = "))
array = [[0 for i in range(n)] for j in range(n)]
visited = [0 for i in range(n)]

mini = 999
u,v = 0,0
total = 0

# Reading the values 
for i in range(n):
    visited[i] = 0
    for j in range(n):
        array[i][j] = int(input())
        if array[i][j] == 0:
            array[i][j] = 999

visited[0] = 1

count = 0
# COUNT IS n-1 BECAUSE EDGES = NO_OF_VERTEX - 1
for count in range(n-1):
    mini = 999
    for i in range(n):
        if visited[i] == 1:
            for j in range(n):
                if visited[j] == 0:
                    if array[i][j] < mini:
                        mini = array[i][j]
                        u = i
                        v = j
    visited[v] = 1
    total += mini
    array[i][j] = array[j][i] = 999
    print("Edge connected ",u,"-->",v," : ",mini)
    
print("Total weight is : ",total)


