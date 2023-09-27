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
    if len(arr) <= 1:                                                      #  4       
        return arr                                                         #  2 
    
    mid = len(arr) // 2                                                    #  6
    left_half = arr[:mid]                                                  #  3 +(n/2)
    right_half = arr[mid:]                                                 #  3 +(n/2) 

    left_half = merge_sort(left_half)                                      #  3 * merge_sort
    right_half = merge_sort(right_half)                                    #  3 * merge_sort
    
    merged = []                                                            #  3 
    left_idx = 0                                                           #  3     
    right_idx = 0                                                          #  3
    
    while left_idx < len(left_half) and right_idx < len(right_half):       #  9 * n +1            
        time+=1
        if left_half[left_idx] < right_half[right_idx]:                    #  5 * n
            merged.append(left_half[left_idx])                             #  4 * n         
            left_idx += 1                                                  #  3 * n     
        else:
            merged.append(right_half[right_idx])                           #  4 * n 
            right_idx += 1                                                 #  3 * n     
            
    time+=len(right_half)-right_idx
    time+=len(left_half)-left_idx
    merged.extend(left_half[left_idx:])                                    #  4 +(numLeft) 
    merged.extend(right_half[right_idx:])                                  #  4 +(numRight)
    
    return merged

my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Original List: ", my_list)
sorted_list = merge_sort(my_list)
print("Sorted array:", sorted_list)

"""
#Grafica mejor caso
x=[]
y=[]
for m in range (1001):
    list1=[]
    for a in range(m):
        list1.append(a);
    time=0
    x.append(m)
    merge_sort(list1)
    y.append(time)
    
plt.plot(x, y)
plt.show()
"""

"""
#Grafica caso promedio
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
""" 


#Gráfica peor caso
x=[]
y=[]
for m in range (1001):
    list1=[]
    for a in range(m):
        list1.append(m-a);
    time=0
    x.append(m)
    merge_sort(list1)
    y.append(time)
    
plt.plot(x, y)
plt.show()
