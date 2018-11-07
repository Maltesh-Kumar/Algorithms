# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 13:48:16 2018

@author: Maltesh_Kumar
"""

n = int(input("Enter dimension n = "))
matrix = [[0 for i in range(n)] for j in range(n)] 

# Initializing all nodes to 0 i.e not visited
visited = [0]*n

# Reading the values
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input())


res = []
# Starting the node from 0
stack = [0]

# Set starting node as visited
visited[0] = 1

# Pop stack 
node = stack.pop(len(stack) - 1);
res.append(node)


while True:
    for x in range (0, len(visited)):
        # Check is path exists and that node is not visited
        if matrix[node][x] == 1 and visited[x] == 0:
            visited[x] = 1
            stack.append(x)
            
# Terminate Loop when Queue is empty	
    if len(stack) == 0:
         break;
    else:
# Pop from Stack
        node = stack.pop(len(stack) - 1)
        res.append(node)

# Print Result         
print(res) 


