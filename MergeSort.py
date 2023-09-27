# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 21:22:16 2023

@author: jsole
"""

import random
import matplotlib.pyplot as plt

time=0
                        
def merge_sort(arr):
    global time
    time+=1
    if len(arr) <= 1:                                                    
        return arr                                                  
    
    mid = len(arr) // 2                                              
    left_half = arr[:mid]                                              
    right_half = arr[mid:]                                                 

    left_half = merge_sort(left_half)                        
    right_half = merge_sort(right_half)                                
    
    merged = []                                                       
    left_idx = 0                                                      
    right_idx = 0                                                      
    
    while left_idx < len(left_half) and right_idx < len(right_half):
        time+=1
        if left_half[left_idx] < right_half[right_idx]:                    
            merged.append(left_half[left_idx])                               
            left_idx += 1                                             
        else:
            merged.append(right_half[right_idx])                          
            right_idx += 1                                              
            
    time+=len(right_half)-right_idx
    time+=len(left_half)-left_idx
    merged.extend(left_half[left_idx:])                                  
    merged.extend(right_half[right_idx:])                                  
    
    return merged

#Complexity -> O(n log n)


my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Original List: ", my_list)
sorted_list = merge_sort(my_list)
print("Sorted array:", sorted_list)


#Average case
x=[]
y=[]
for m in range (1001):
    list1=[]
    for a in range(m):
        list1.append(random.randint(-1000, 1000));
    time=0
    x.append(m)
    merge_sort(list1)
    y.append(time)
    
plt.plot(x, y)
plt.show()



