# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 18:10:34 2018

@author: Maltesh_Kumar
"""

import time
import threading

##########################################################################

def square(a):
    for i in a:
        # USING SLEEP SO THAT FXN'S DON'T CONFLICT WHEN EXECUTING
        time.sleep(0.2) 
        print("Square of ",i," = ",i**2)
        
def cube(a):
    for i in a:
        # USING SLEEP SO THAT FXN'S DON'T CONFLICT WHEN EXECUTING
        time.sleep(0.2)
        print("Cube of ",i," = ",i**3)
        
##########################################################################
        
# THIS IS A BASIC GENERAL METHOD WHERE WE CALL THE FXN 
# FIRST SQUARE THEN CUBE FXN IS EXECUTED 
a = [1,2,3,4,5,6,7,8,9]
start_time = time.time()
square(a)
cube(a)
stop_time = time.time()
print("Time taken = ", stop_time - start_time)

#########################################################################

# THIS IS WHERE WE MAKE USE OF THREAD TO PROCESS BOTH FXN TOGETHER
t_start = time.time()
t1 = threading.Thread(target = square, args = (a,))
t2 = threading.Thread(target = cube, args = (a,))

t1.start() 
# THIS IS JUST TO MAINTAIN A SMALL GAP B/W 2 THREADS SO THEY PRINT IN ORDER
time.sleep(0.01)
t2.start()

# WE USE JOIN TO TELL MAIN FXN NOT TO PROCESS ANYTHING FURTHUR UNTIL... 
# .... THREADS HAVE FINISHED THEIR PROCESSING
t1.join()
t2.join()
t_stop = time.time()
print("Time taken = ",t_stop - t_start)

#########################################################################

























