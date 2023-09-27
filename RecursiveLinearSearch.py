# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 19:53:47 2023

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
    
    
def recursive_linear_search_nums(arr, x, i):
    global time
    time+=1
    if(i>=len(arr)):                                               
        return -1
    elif(arr[i].num==x):                                            
        return i
    else:
        return recursive_linear_search_nums(arr, x, i+1)           

#### Complexity -> O(n)


def recursive_linear_search_strings(arr, cadena1, i):
    global time
    time+=1
    if(i>=len(arr)):                                                      
        return -1
    elif(arr[i].name==cadena1):                                            
        return i
    else:
        return recursive_linear_search_strings(arr, cadena1, i+1)           

#### Complexity-> O(n)

print("Element 700 is in position: " +str(recursive_linear_search_nums(nodes, 700, 0)))
print("Element 9574 is in position: " +str(recursive_linear_search_nums(nodes, 9574, 0)))
print("Element 2 is in position: " + str(recursive_linear_search_nums(nodes, 2, 0)))

print("Element Dall is in position: " +str(recursive_linear_search_strings(nodes, "Dall", 0)))
print("Element Ebenezer is in position: " +str(recursive_linear_search_strings(nodes, "Ebenezer", 0)))
print("Element AAAAAA is in position: " + str(recursive_linear_search_strings(nodes, "AAAAAAA", 0)))


     
####     NUMS   #####
'''
#Best case
x=[]
y=[]
for m in range (1, 1001):
    time=0
    random.shuffle(nodes)
    nodeList=nodes[:m]
    recursive_linear_search_nums(nodeList, nodeList[0].num, 0)
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
    recursive_linear_search_nums(nodeList, random.randint(1, m+1), 0)
    x.append(m) 
    y.append(time)

plt.plot(x, y)
plt.show()
'''
'''
#Worst Case
x=[]
y=[]
for m in range (1, 1001):
    time=0
    random.shuffle(nodes)
    nodeList=nodes[:m]
    recursive_linear_search_nums(nodeList, 1000000, 0)   # elemento que no está en la lista
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
    recursive_linear_search_strings(nodeList, nodeList[0].name, 0)  
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
    recursive_linear_search_strings(nodeList, nodeList[random.randint(0, m-1)].name, 0)  
    x.append(m) 
    y.append(time)

plt.plot(x, y)
plt.show()
'''

'''
#Worst Case
x=[]
y=[]
for m in range (1, 1001):
    time=0
    random.shuffle(nodes)
    nodeList=nodes[:m]
    recursive_linear_search_strings(nodeList, "AAAAAAAAAAAAA", 0)   # elemento que no está en la lista
    x.append(m) 
    y.append(time)

plt.plot(x, y)
plt.show()
'''