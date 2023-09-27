# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:21:50 2023

@author: arns
"""
import sys
import random
import matplotlib.pyplot as plt
sys.setrecursionlimit(1500)

time=0

def partition(arr, low, high):
    global time
    pivot = arr[low]                                                       
    left = low + 1                                                           
    right = high                                                                     
    done = False                                                           
                                                                                  
    while not done:                                                                         
        time+=1                                                                                     
        while left <= right and arr[left] <= pivot:                                         
            time+=1                                                                              
            left += 1                                                                  
                                                                                            
        while arr[right] >= pivot and right >=left:                                       
            time+=1                                                                            
            right -= 1                                                                    
                                                                                                  
        if right < left:                                                          
            done= True                                                      
        else:                                                                 
            arr[left], arr[right] = arr[right], arr[left]                    
                                                                                 
            
    arr[low], arr[right] = arr[right], arr[low]                                             
    return right 

#Complexity Partition->O(n)

def quick_sort(arr, low, high):
    global time
    time+=1
    if low < high:                                                           
        pivot_index = partition(arr, low, high)                              
                                                                           
                                                                             
        quick_sort(arr, low, pivot_index - 1)                                          
        quick_sort(arr, pivot_index + 1, high)                                         

#Complexity Quick Sort Average Case-> O(n log n)
#Complexity Quick Sort Worst Case-> O(n^2)

my_list = [42, 17, 33, 13, 29, 21, 8, 55, 5, 18]
print("Original List: ", my_list)
quick_sort(my_list, 0, 9)
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
    quick_sort(list1, 0, m-1)
    y.append(time)
    
plt.plot(x, y)
plt.show()



#Worst Case
x=[]
y=[]
for m in range (1001):
    list1=[]
    for a in range(m):
        list1.append(m-a);
    time=0
    x.append(m)
    quick_sort(list1, 0, m-1)
    y.append(time)
    
plt.plot(x, y)
plt.show()
