# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 18:27:29 2018

@author: Maltesh_Kumar
"""

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n > 0:
        TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
        print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
        TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
    
n = int(input("Enter number of disc = "))
TowerOfHanoi(n, 'A', 'C', 'B')