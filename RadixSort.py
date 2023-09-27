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
    

def radix_sort_strings(arr):
    global time
    max_len=0                                                                    # 3   
    for v in arr:                                                                # n   
        time+=1                                                 
        if max_len < (len(v.name)):                                              # 4n           
            max_len=len(v.name)                                                  # 3n   

##Denoting max_len as k

    for exp in range(max_len - 1, -1, -1):                                       # k
        n = len(arr)                                                             # 4k   
        output = [0] * n                                                         # n*k
        count = [0] * 256                                                        # 256*k
        time+=1
        for i in range(n):                                                       # 3n*k
            time+=1
            index = ord(arr[i].name[exp]) if exp < len(arr[i].name) else 0       # 10n*k
            count[index] += 1                                                    # 4n*k   

        for i in range(1, 256):                                                  # 256*k   
            time+=1                                                              
            count[i] += count[i - 1]                                             # 256*k

        i = n - 1                                                                # 3k   
        while i >= 0:                                                            # 3n*k   
            time+=1                             
            index = ord(arr[i].name[exp]) if exp < len(arr[i].name) else 0       # 10n*k
            output[count[index] - 1] = arr[i]                                    # 7n*k       
            count[index] -= 1                                                    # 5n*k       
            i -= 1                                                               # 3n*k
        arr=output                                                               # n*k

    return arr
######### Complexity-> O(n*k) 

######### Space Complexity -> O(n+256)-> O(n)


def radix_sort_nums(arr):
    global time
    max_len=0                                                                    # 3   
    for v in arr:                                                                # 3n
        a=(len(str(v.num)))                                                      # 3n+m (sum of lengths of all strings) 
        if max_len < a:                                                          # 3n
            max_len=a                                                            # 2n
    
    exp=1                                                                        # 3
    
    ###### Next for loop repeats log10(max) times because biggest number has log10 digits. 
    ###### Strictly speaking log10+1 digits
    
    for j in range(max_len - 1, -1, -1):                                         # log10(max)       
        time+=1   
        n=len(arr)                                                               # 4 *log10(max)
        output = [0] * n                                                         # n*log10(max)
        count = [0] * 10                                                         # 40*log10(max)                             
        for i in range(n):                                                       # 3*log10(max)*n   
            time+=1
            index = ((arr[i].num//exp)%10) if exp <= arr[i].num else 0           # 10*log10(max)*n   
            count[index] += 1                                                    # 4*log10(max)*n

        for i in range(1, 10):                                                   # 10*log10(max)
            time+=1
            count[i] += count[i - 1]                                             # 6*log10(max)

        i = n - 1                                                                # 4*log10(max)
        while i >= 0:                                                            # 3*log10(max)*n   
            time+=1 
            index = ((arr[i].num//exp)%10) if exp <= arr[i].num else 0           # 10*log10(max)*n   
            output[count[index] - 1] = arr[i]                                    # 7*log10(max)*n       
            count[index] -= 1                                                    # 5*log10(max)*n
            i -= 1                                                               # 3*log10(max)*n
            
        arr=output                                                               # log10(max)*n
        exp*=10
        
    return arr

######### Complexity-> O(n*k) or O(n*log10(max)) 

######### Space Complexity -> O(n+10)-> O(n)


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

"""
#Mejor Caso Nums
x=[]
y=[]
for m in range (1001):
    time=0
    nodeList=nodes[:m]
    sortedList=radix_sort_nums(nodeList)
    x.append(m) 
    y.append(time)

plt.plot(x, y)
plt.show()
"""
"""
#Caso Promedio Nums
x=[]
y=[]
random.shuffle(nodes)
for m in range (1001):
    time=0
    nodeList=nodes[:m]
    random.shuffle(nodeList)
    sortedList=radix_sort_nums(nodeList)
    x.append(m)
    y.append(time)

plt.plot(x, y)
plt.show()
"""
"""
#Peor caso Nums
x=[]
y=[]
for m in range (1001):
    time=0
    nodeList=nodes[:m]
    nodeList.reverse()
    sortedList=radix_sort_nums(nodeList)
    x.append(m)
    y.append(time)

plt.plot(x, y)
plt.show()
"""

############################CADENAS##########################
"""
nodes.sort(key=lambda x: x.name)
#Mejor caso Strings
x=[]
y=[]
for m in range (1, 1001):
    time=0
    nodeList=nodes[:m]
    sortedList=radix_sort_strings(nodeList)
    x.append(m)
    y.append(time)

for a in sortedList:
    print(a)
plt.plot(x, y)
plt.show()
"""
"""
#Caso promedio Strings
x=[]
y=[]
random.shuffle(nodes)
for m in range (1, 1001):
    time=0
    nodeList=nodes[:m]
    sortedList=radix_sort_strings(nodeList)
    x.append(m)
    y.append(time)

plt.plot(x, y)
plt.show()
"""
"""
#Peor caso Strings
nodes.sort(key=lambda x: x.name)
nodes.reverse()

#Mejor caso Strings
x=[]
y=[]
for m in range (1, 1001):
    time=0
    nodeList=nodes[:m]
    sortedList=radix_sort_strings(nodeList)
    x.append(m)
    y.append(time)

plt.plot(x, y)
plt.show()
for a in sortedList:
    print(a)
"""
"""
random.shuffle(nodes)
nodes1=radix_sort_nums(nodes)
for a in nodes1:
    print(a)
"""
