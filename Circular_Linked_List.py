# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:02:17 2018

@author: Maltesh_Kumar
"""


class node:
    def __init__(self,data):
        self.data = data
        self.next = None


# Initializing the node before appending it to Linked_List     
class circular_linked_list:
    def __init__(self):
        self.head = None
        print(self.head)

# Appending the values into Linked_List
# cur = "current"        
    def append(self,data):
        if self.head == None:
            self.head = node(data)
            self.head.next = self.head
        else:
            cur = self.head
            new_node = node(data)
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

# Displaying values of Linked_List            
    def display(self):
            cur = self.head
            ele = []
            while cur.next != None:
                ele.append(cur.data)
                cur = cur.next
                if cur == self.head:
                    break
            print(ele)
        
# Displaying length of Linked_List         
    def length(self):
        total = 1
        cur = self.head
        while cur.next != self.head:
            total += 1
            cur = cur.next
        return total

# Fetching values in Linked_List    
    def get(self,index):
        idx = 1
        if index > self.length():
            print("Index out of bound")
            return
        cur = self.head
        while cur.next != self.head:
            if idx == index:
                print(cur.data)
            idx += 1
            cur = cur.next 
            
# Erasing a perticular value in Linked_List     
    def erase(self,index):
        idx = 2
        cur = self.head
        temp = self.head.next 
        if index == 1:
          #  self.head = cur.next 
            while cur.next != self.head:
                cur = cur.next  
            cur.next = self.head.next
            self.head = temp 
            return
        else:
            while cur.next != self.head:
                prev = cur 
                cur = cur.next 
                if idx == index:
                    prev.next = cur.next  
                idx += 1
            
            
    
# Input Section    
# cll is a variable and can be anything        
cll = circular_linked_list()

cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
cll.append(5)

cll.length()

cll.display()

cll.get(5)

cll.erase(3)

            
















ss










