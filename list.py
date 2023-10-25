# -*- coding: utf-8 -*-
"""List.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11dOnigAKDZy2A6HQsPFxYbBLJptefSAk
"""

#List --- []

list_1 = ["apple","banana","orange"]
print(type(list_1))
print(list_1)

print(len(list_1))

list_2 = ["apple",1,2.5,False]
print(list_2 )

list_2 = ["apple",1,2.5,False]#0,1,2,3 --n-1 (left to right)
#           -4,  -3, -2 ,-1(right to left)

print(list_2[0])

print(list_2[3])

#slicing ---range of items
list_3 = ["apple",1,2.5,False,"orange","bananna",78,100]#1,5
print(list_3[1:6])#1 t0 6(1 to 5)

#slicing ---range of items
list_3 = ["apple",1,2.5,False,"orange","bananna",78,100]#1,5
print(list_3[1:5])#1 t0 6(1 to 5)

#slicing ---range of items
list_3 = ["apple",1,2.5,False,"orange","bananna",78,100]#1,5
print(list_3[2:7])#1 t0 6(1 to 5)

list_3 = ["apple",1,2.5,False,"orange","bananna",78,100]
print(list_3[2:])

list_3 = ["apple",1,2.5,False,"orange","bananna",78,100]
print(list_3[:4])#3

list_3 = ["apple",1,2.5,False,"orange","bananna",78,100]
print(list_3[-1])

list_3 = ["apple",1,2.5,False,"orange","bananna",78,100]
print(list_3[3:-2])

list_3 = ["apple",1,2.5,False,"orange","bananna",78,100]
print(list_3[:-2])

list_3 = ["apple",1,2.5,False,"orange","bananna",78,100]
print(list_3[-1:6])

list_3 = ["apple",1,2.5,False,"orange","bananna",78,100]
print(list_3[::-1])

str = "hello"
print(str[::-1])

a = [1,2,3,4,54]
a[1] = 10
print(a)

a.append("orange")
print(a)

a.append(100)
print(a)

a.insert(1,2)
print(a)

a.append([100,1000,111])
print(a)

a.extend([100,1000,11])
print(a)

print(a[8][0])

print(a[8][2])

a.remove("orange")
print(a)

a.pop(7)
print(a)

del a[0]
print(a)

a.clear()
print(a)

del a
print(a)

A = [1,2,3,4,5]
B= A.copy()
print(A)
print(B)

C = A
print(C)

D = list(A)
print(D)

F = list((4,5,6,7,8))
print(F)

print(type(F))

a = [1,14,6,2,5,8,3]
a.sort()
print(a)

a.sort(reverse = True)
print(a)

a = [1,14,6,2,5,8,3,1]
print(a.count(1))

print(a.count(5))

a = [1,14,6,2,5,8,3,1]
print(a.index(1))

a = [1,14,6,2,1,8,3,1]#14,6,2,1
print(a.index(1,1,7))#value,start point,end point

a = [1,14,6,1,2,1,8,3,1]#14,6,2,1
#1 - index
# 1 --7  (14,6,2,1,8,3)===1
#0-1
#1-14
#2-6
#4-1

print(a.index(1,1,7))#value,start point,end point

a = [1,14,6,2,1,8,3,1]

for i in a:#1,14,6,2,1,8,3,1,
  print(i)

for j in range (len(a)):
  print(a[j])

i = 0
while i < len(a):#0 <8---1<8
  print(a[i])
  i +=1# i = i+1=0+1=1 = 1+1=2

print(a)

for a in b:
  print(b)

b = []
for i in a:
  b.append(i)
print(b)

newlist = [x for x in a]
print(newlist)

newlist_1 = [x for x in a if x >10]
print(newlist_1)

#newlist = [expression for item in iterable if condition == true]

list_1 = ["a","b","c"]
list_2 = [1,2,3]
list_3 = list_1 +list_2
print(list_3)

list_2 = [1,2,3]
list_2 = list_2*5#3,6,9
print(list_2)

list_a = []
for i in range(len(list_2)):
  b = i *3
  list_a.append(b)
print(list_a)
print(list_2)

p = [100,5,8,99,47,58,69,78]
print(max(p))

p = [100,5,8,99,47,58,69,78]
print(min(p))

p = ["a","b","c"]
print(max(p))

p = ["a","b","c"]
print(min(p))

p = ["a","B","c"]
print(max(p))

p = ["a","B","c"]
print(min(p))

p = ["a","B","c","c"]
print((p))

#lowera-min,b,c-max ,upper
#list -mutable-changeble,you add any element in any possision
'''
ordered
changeble
allow duplicate values
any datatype
index
'''

a = [1,2,3,4]
a^b
b^a
a^b