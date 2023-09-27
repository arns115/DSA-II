# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 20:45:27 2023

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
        
    
def counting_sort_strings(arr):
    global time
    count = [0] * 257;                                                          # 257            
    for v in arr:                                                               # n        
        time+=1                                                                     
        index = ord(v.name[0])                                                  # 6n    
        count[index] += 1                                                       # 5n

    for i in range(1, 257):                                                     # 257
        time+=1                                                         
        count[i] += count[i - 1]                                                # 6n        

    n = len(arr)                                                                # 4
    output = [''] * n                                                           # n 
    for i in range(n - 1, -1, -1):                                              # n    
        time+=1 
        index = ord(arr[i].name[0])                                             # 6n
        output[count[index] - 1] = arr[i]                                       # 7n
        count[index] -= 1                                                       # 5n    

    return output

######### Complexity-> O(n) 

######### Space Complexity -> O(n+256)-> O(n)

def counting_sort_nums(arr):
    global time
    max_val=0                                                                   # 3    
    for v in arr:                                                               # n        
        time+=1
        if max_val<v.num:                                                       # 3n
            max_val=v.num                                                       # 2n
            
    range_of_elements = max_val+1                                               # 4

    count_arr = [0] * range_of_elements                                         # 4*max(array)

    for v in arr:                                                               # n    
        time+=1
        count_arr[v.num] += 1                                                   # 5n

    for i in range(1, range_of_elements):                                       # max(array)        
        time+=1
        count_arr[i] += count_arr[i - 1]                                        # 6*max(array)
        
    sorted_arr = [0]*len(arr)                                                   # 4n
    for v in arr:                                                               # n
        time+=1
        sorted_arr[count_arr[v.num]-1]=v                                        # 7n 
        count_arr[v.num]-=1                                                     # 5n

    return sorted_arr

######### Complexity-> O(n+m) 

######### Space Complexity -> O(n+m)-> O(n+m)


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
    


#Average case Nums

x=[]
y=[]
random.shuffle(nodes)

for m in range (1, 1001):
    time=0
    nodeList=nodes[:m]
    sortedList=counting_sort_nums(nodeList)
    x.append(m)
    y.append(time)

plt.plot(x, y)
plt.show()



############################    STRINGS  ##########################


#Caso promedio Strings
x=[]
y=[]
random.shuffle(nodes)
for m in range (1, 1001):
    time=0
    nodeList=nodes[:m]
    sortedList=counting_sort_strings(nodeList)
    x.append(m)
    y.append(time)

plt.plot(x, y)
plt.show()


random.shuffle(nodes)
nodes1=counting_sort_nums(nodes)
for a in nodes1:
    print(a)

nodes1=counting_sort_strings(nodes)
for a in nodes1:
    print(a)
