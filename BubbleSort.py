# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 19:20:25 2023

@author: arns
"""
import random
import matplotlib.pyplot as plt

time =0
def bubble_sort(arr):
    global time
    n = len(arr)                                                      
    i = 0                                                            
    j = 0                                                          
    aux=0                                                         
    while i<n:                                                        
        time+=1                                         
        j=0                                                             
        while j<n-i-1:                                               
            time+=1                                                 
            if arr[j]>arr[j+1]:                                        
                aux=arr[j]                                           
                arr[j]=arr[j+1]                                     
                arr[j+1]=aux                                           
            j+=1                                                        
        i+=1                                                           
    return arr



list1=[]
for a in range (10):
    list1.append(10-a)

print("Original list :", list1)
sortedList=bubble_sort(list1)
print("Ordered List", sortedList)

#Grafica Average Case

x=[]
y=[]
for m in range (1001):
    list1=[]
    time=0
    for a in range(m):
        list1.append(random.randint(-1000, 1000))
    x.append(m)
    bubble_sort(list1)
    y.append(time)
    
plt.plot(x, y)
plt.show()
