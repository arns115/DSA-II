# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 20:04:45 2023

@author: arns
"""

import random
import csv
import matplotlib.pyplot as plt

time=0

class node:
    def __init__(self, num, name, email, gender):
        self.num=num
        self.name=name
        self.email=email
        self.gender=gender
        
    def __str__(self): 
        return  "% s-% s-% s-% s" % (self.num, self.name, self.email, self.gender) 
    
file=open('MOCK_DATA.csv')
csvreader=csv.reader(file)
header=[] 
header=next(csvreader)
nodes=[]
rows=[]
for row in csvreader:
    rows.append(row)
for r in rows:
    node1=node(int(r[0]), r[1], r[2], r[3]);
    nodes.append(node1)
    
############  NUMS ###############

def bubble_sort_nums(arr):
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
            if arr[j].num>arr[j+1].num:                               
                aux=arr[j]                                             
                arr[j]=arr[j+1]                                        
                arr[j+1]=aux                                           
            j+=1                                                       
        i+=1                                                           

#Complxity-> O(n^2)

def heap_sort_nums(arr):
    global time
    n = len(arr)                                                        
    for i in range(n // 2 - 1, -1, -1):                              
        heapify_nums(arr, n, i)                                        
    
    for i in range(n - 1, 0, -1):                                    
        time+=1
        arr[i], arr[0] = arr[0], arr[i]                                     
        heapify_nums(arr, i, 0)                                     

#Complexity heap_sort-> O(n log n)


def heapify_nums(arr, n, root):                                        
    global time
    time+=1    
    largest = root                                               
    left = 2 * root + 1                                                 
    right = 2 * root + 2                                         
    
    if left < n and arr[left].num > arr[largest].num:                 
        largest = left                                             
    
    if right < n and arr[right].num > arr[largest].num:                 
        largest = right                                               
    
    if largest != root:                                               
        arr[root], arr[largest] = arr[largest], arr[root]             
        heapify_nums(arr, n, largest)                                                

#Complexity heapify-> O(log n)

############# STRINGS #############

def bubble_sort_strings(arr):
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
            if arr[j].name>arr[j+1].name:                              
                aux=arr[j]                                             
                arr[j]=arr[j+1]                                        
                arr[j+1]=aux                                           
            j+=1                                                      
        i+=1                                                           


#Complxity-> O(n^2)

def heap_sort_strings(arr):
    global time
    n = len(arr)                                                   
    for i in range(n // 2 - 1, -1, -1):                                
        heapify_strings(arr, n, i)                                     
    
    for i in range(n - 1, 0, -1):                                          
        time+=1
        arr[i], arr[0] = arr[0], arr[i]                             
        heapify_strings(arr, i, 0)                                    

#Complexity heap_sort-> O(n log n)


def heapify_strings(arr, n, root):                                     
    global time
    time+=1    
    largest = root                                           
    left = 2 * root + 1                                              
    right = 2 * root + 2                                       
    
    if left < n and arr[left].name > arr[largest].name:               
        largest = left                                               
    
    if right < n and arr[right].name > arr[largest].name:              
        largest = right                                                 
    
    if largest != root:                                                 
        arr[root], arr[largest] = arr[largest], arr[root]             
        heapify_strings(arr, n, largest)                                                

#Complexity heapify-> O(log n)


def iterative_binary_search_nums(arr, x):
    global time
    l=0                                                               
    r=len(arr)-1                                                       
    while(l<=r):                                                  
        time+=1                     
        mid=(l+r)//2                                               
        if(arr[mid].num==x):                                           
            return mid
        elif((arr[mid].num)>x):                                      
            r=mid-1                                                
        else:
            l=mid+1                                                 
            
    return -1
    
## Complexity-> O(log n)


def iterative_binary_search_strings(arr, x):
    global time
    l=0
    r=len(arr)-1
    while(l<=r):
        time+=1
        mid=(l+r)//2
        if(arr[mid].name==x):
            return mid
        elif((arr[mid].name)>x):
            r=mid-1
        else:
            l=mid+1
            
    return -1
    
## Complexity-> O(log n)

heap_sort_nums(nodes)
print("Element 700 is in position: " +str(iterative_binary_search_nums(nodes, 700)))
print("Element 9574 is in position: " +str(iterative_binary_search_nums(nodes, 9574)))
print("Element 2 is in position: " + str(iterative_binary_search_nums(nodes, 2)))

heap_sort_strings(nodes)
print("Element Dall is in position: " +str(iterative_binary_search_strings(nodes, "Dall")))
print("Element Ebenezer is in position: " +str(iterative_binary_search_strings(nodes, "Ebenezer")))
print("Element AAAAAA is in position: " + str(iterative_binary_search_strings(nodes, "AAAAAAA")))
############ NUMEROS ####################

# BUBBLE SORT

#Average case with Bubble Sort
x=[]
y=[]
for m in range (1, 1001):
    time=0
    nodeList=nodes[:m]
    random.shuffle(nodeList)
    bubble_sort_nums(nodeList)
    iterative_binary_search_nums(nodeList, random.randint(1, m+1))
    x.append(m) 
    y.append(time)

plt.plot(x, y)
plt.show()



#Average case with Heap Sort
x=[]
y=[]
for m in range (1, 1001):
    time=0
    nodeList=nodes[:m]
    random.shuffle(nodeList)
    heap_sort_nums(nodeList)
    iterative_binary_search_nums(nodeList, random.randint(1, m+1))
    x.append(m) 
    y.append(time)

plt.plot(x, y)
plt.show()


#######  STRINGS #########

# BUBBLE SORT

#Average case with Bubble Sort
x=[]
y=[]
for m in range (1, 1001):
    time=0
    nodeList=nodes[:m]
    random.shuffle(nodeList)
    bubble_sort_strings(nodeList)
    iterative_binary_search_strings(nodeList, nodes[random.randint(1, m+1)].name)
    x.append(m) 
    y.append(time)

plt.plot(x, y)
plt.show()


############ HEAP SORT ################


#Average case with Heap Sort
x=[]
y=[]
for m in range (1, 1001):
    time=0
    nodeList=nodes[:m]
    random.shuffle(nodeList)
    heap_sort_strings(nodeList)
    iterative_binary_search_strings(nodeList, nodes[random.randint(1, m+1)].name)
    x.append(m) 
    y.append(time)

plt.plot(x, y)
plt.show()

