# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:22:29 2023

@author: arns
"""

import random
import matplotlib.pyplot as plt

time=0

def heap_sort(arr):
    global time
    n = len(arr)                                                        
    for i in range(n // 2 - 1, -1, -1):                        
        heapify(arr, n, i)                                        
    
    for i in range(n - 1, 0, -1):                                        
        time+=1
        arr[i], arr[0] = arr[0], arr[i]                                 
        heapify(arr, i, 0)                                              

#Complexity heap_sort-> O(n log n)

def heapify(arr, n, root):                                             
    global time
    time+=1    
    largest = root                                                   
    left = 2 * root + 1                                                 
    right = 2 * root + 2                                              
    
    if left < n and arr[left] > arr[largest]:                  
        largest = left                                              
    
    if right < n and arr[right] > arr[largest]:                        
        largest = right                                                
    
    if largest != root:                                                
        arr[root], arr[largest] = arr[largest], arr[root]               
        heapify(arr, n, largest)                                                

#Complexity heapify-> O(log n)

my_list = [42, 17, 33, 13, 29, 21, 8, 55, 5, 18]
print("Original List: ", my_list)
heap_sort(my_list)
print("Sorted array:", my_list)


#Average Case
x=[]
y=[]
for m in range (1001):
    list1=[]
    for a in range(m):
        list1.append(random.randint(-1000, 1000));
    time=0
    x.append(m)
    heap_sort(list1)
    y.append(time)
    
plt.plot(x, y)
plt.show()


