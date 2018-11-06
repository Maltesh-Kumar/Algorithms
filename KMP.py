# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 12:25:58 2018

@author: Maltesh_Kumar
"""


#  KMP Algorithm 
def KMP(pattern, text): 
    x = len(pattern) 
    y = len(text) 
  
# lps = longest prefix suffix  
    lps = [0]*x 
    j = 0 # index for pat[] 
  
    # Preprocess the pattern (calculate lps[] array) 
    LPSArray(pat, x, lps) 
  
    i = 0 # index for txt[] 
    while i < y: 
        if pattern[j] == text[i]: 
            i += 1
            j += 1
  
        if j == x: 
            print("Found pattern at index " + str(i-j)) 
            j = lps[j-1] 
  
# mismatch occuring if there is not match between i & j 
        elif i < y and pattern[j] != text[i]: 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1 
 
    
def LPSArray(pattern, x, lps): 
# l holds length of the previous longest prefix suffix
    l = 0 
    lps[0] = 0  
    i = 1
  
# the loop calculates lps[i] for i = 1 to x-1 
    while i < x: 
        if pattern[i] == pattern[len]: 
            l += 1
            lps[i] = l
            i += 1
        else: 
            if l != 0: 
                l = lps[l-1]  
            else: 
                lps[i] = 0
                i += 1


# Input Section  
text = "ABABCABCABABABD"
pattern = "ABABD"
KMP(pattern, text)


