# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 19:15:03 2023

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
    
def iterative_linear_search_nums(arr, x):
    global time
    for i in range(len(arr)):                                     
        time+=1 
        if(arr[i].num==x):                                           
            return i
    return -1

#### Complexity -> O(n)


def iterative_linear_search_strings(arr, cadena1):
    global time
    for i in range(len(arr)):                                     
        time+=1
        if(arr[i].name==cadena1):                                  
            return i
    return -1

#### Complexity-> O(n)


print("Element 700 is in position: " +str(iterative_linear_search_nums(nodes, 700)))
print("Element 9574 is in position: " +str(iterative_linear_search_nums(nodes, 9574)))
print("Element 2 is in position: " + str(iterative_linear_search_nums(nodes, 2)))

print("Element Dall is in position: " +str(iterative_linear_search_strings(nodes, "Dall")))
print("Element Ebenezer is in position: " +str(iterative_linear_search_strings(nodes, "Ebenezer")))
print("Element AAAAAA is in position: " + str(iterative_linear_search_strings(nodes, "AAAAAAA")))

####     NUMS   #####
'''
#Best case
x=[]
y=[]
for m in range (1, 1001):
    time=0
    random.shuffle(nodes)
    nodeList=nodes[:m]
    iterative_linear_search_nums(nodeList, nodeList[0].num)
    x.append(m) 
    y.append(time)

plt.plot(x, y)
plt.show()
'''
'''
#Average Case
x=[]
y=[]
for m in range (1, 1001):
    time=0
    nodeList=nodes[:m]
    random.shuffle(nodeList)
    iterative_linear_search_nums(nodeList, random.randint(1, m+1))
    x.append(m) 
    y.append(time)

plt.plot(x, y)
plt.show()
'''
'''
#Worst case
x=[]
y=[]
for m in range (1, 1001):
    time=0
    random.shuffle(nodes)
    nodeList=nodes[:m]
    iterative_linear_search_nums(nodeList, 1000000)   # elemento que no está en la lista
    x.append(m) 
    y.append(time)

plt.plot(x, y)
plt.show()
'''
####### STRINGS #######
'''

#Best case
x=[]
y=[]
for m in range (1, 1001):
    time=0
    random.shuffle(nodes)
    nodeList=nodes[:m]
    iterative_linear_search_strings(nodeList, nodeList[0].name)  
    x.append(m) 
    y.append(time)

plt.plot(x, y)
plt.show()
'''

'''
#Average Case
x=[]
y=[]
for m in range (1, 1001):
    time=0
    nodeList=nodes[:m]
    random.shuffle(nodeList)
    iterative_linear_search_strings(nodeList, nodeList[random.randint(0, m-1)].name)  
    x.append(m) 
    y.append(time)

plt.plot(x, y)
plt.show()
'''
'''
#Worst case
x=[]
y=[]
for m in range (1, 1001):
    time=0
    random.shuffle(nodes)
    nodeList=nodes[:m]
    a=iterative_linear_search_strings(nodeList, "AAAAAAAAAAAAA")   # elemento que no está en la lista
    x.append(m) 
    y.append(time)
plt.plot(x, y)
plt.show()
'''

