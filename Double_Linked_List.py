# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 13:32:46 2018

@author: Maltesh_Kumar
"""



# Initializing the node before appending it to Linked_List
# prev = "previous"
class node:
    def __init__(self,data = None):
        self.prev = None
        self.data = data
        self.next = None

        
class doublelinkedlist:
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
        new_node.prev = cur 
        new_node.next = None
        
# Displaying values of Linked_List
    def display(self):
        cur = self.head
        ele = []
        while cur.next != None:
            cur = cur.next
            ele.append(cur.data)
        print(ele)

# Displaying length of Linked_List       
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            cur = cur.next
            total += 1  
        return total
    
#  Displaying values in reverse order of Linked_List  
    def disp_reverse(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        pele = []
        while cur.prev != None:
            pele.append(cur.data)
            cur = cur.prev
        print(pele)
        
# Fetching values in Linked_List
    def get(self,index):
        cur = self.head
        if index > self.length() or index < 1:
            print("Error in range")
            return
        idx = 1
        while cur.next != None:
            cur = cur.next
            if idx == index:
                print(cur.data)
            idx += 1

# Adding values in any index in Linked_List   
# ci = current_index
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
                    cur.prev = new_node 
                    new_node.next = cur 
                    new_node.prev = prev 
                ci += 1

# Erasing a perticular value in Linked_List  
    def erase(self,index):
        cur = self.head
        if index > self.length():
            print("Error in range")
            return
        idx = 1
        while True:
            prev = cur 
            cur = cur.next
            if idx == index:
                prev.next = cur.next
                temp = cur.next
                temp.prev = prev
                return
            idx += 1
    

# Input Section    
# dll is a variable and can be anything
dll = doublelinkedlist()

dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)

dll.length()

dll.display()
dll.disp_reverse()

dll.get(4)

dll.erase(3)

dll.add(3,777)
        














