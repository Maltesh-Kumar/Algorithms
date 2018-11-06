# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 12:45:32 2018

@author: Maltesh_Kumar
"""



# Initializing the node before appending it to Linked_List
class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        

        
class linkedlist:
    def __init__(self):
        self.head = node()

# Appending the values into Linked_List
# cur = "current"        
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

# Displaying length of Linked_List          
    def length(self):
        count = 0
        cur = self.head
        while cur.next != None:
            count += 1
            cur = cur.next
        return count

# Displaying values of Linked_List        
    def display(self):
        a = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            a.append(cur.data)
        print(a)

# Fetching values in Linked_List   
# cur_idx = "current_index"
    def get(self,index):
        if index > self.length():
            print("Out of range error")
            return None
        cur_idx = 1
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if cur_idx == index:
                print(cur.data)
            cur_idx += 1
            
# Adding values in any index in Linked_List     
    def add(self,index,value):
            if index+1 > self.length():
                print("Not Possible")
                return
            cur = self.head
            ci = 1
            new_node = node(value)
            while cur.next != None:
                prev = cur
                cur = cur.next
                if ci == index:
                    prev.next = new_node
                    new_node.next = cur 
                ci += 1

# Erasing a perticular value in Linked_List              
    def erase(self,index):
        if index > self.length():
            print("Out of range error")
        cur_idx = 1
        cur = self.head
        while True:
            last = cur
            cur = cur.next 
            if cur_idx == index:
                last.next = cur.next
                return
            cur_idx += 1
        
        
        
# Input Section    
# dll is a variable and can be anything        
sll = linkedlist()

sll.append(1)     
sll.append(2)        
sll.append(3)        
sll.append(4)    

sll.display()    

sll.length()

sll.get(4)

sll.erase(2)

sll.add(4,333)




