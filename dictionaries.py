# -*- coding: utf-8 -*-
"""Dictionaries.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HxmfuIMwYQzS5dK6we-O-E7k9GXY0DQA
"""

list1 = []
tuple1 = (1, 2, 3, 4, 5)

for i in tuple1:
    x = i + 5
    list1.append(x)

print(list1)

#Count
tuple1 = (1, 2, 3, 4, 5,1,1)
print(tuple1.count(1))

#index
print(tuple1.index(4))

"""##thisdict = {"car1":"ford","car2":"benz","car3":"lakshmi"}"""

#{}
thisdict = {"car1":"ford","car2":"benz","car3":"lakshmi"}
print(thisdict)

"""
change
not allowed duplicates --key , allow duplicates -values
>3.0 on ordered
update
delete
"""

print(type(thisdict))

print(len(thisdict))

dict1 = {"brand": "ford",
          "electric": "false",
          "year":1964,
          "colors":["red","white","blue","red"]
          }
print(dict1)

dict2 = {"brand": "ford",
         "brand": "ford",
          "electric": "false",
          "year":1964,
          "colors":["red","white","blue","red"]
          }
print(dict2)

a = dict(name = "laksmi",country = "india",number = 123456)
print(a)

list = [1,2,3]
print(list[2])

print(a["name"])

print(a.get("name"))

print(a.keys())

print(a.values())

print(a.items())

a["name"] = "dodda"
print(a)

a.update({"name":"lakshmi"})
print(a)

a["car"] = "benz"
print(a)

a.update({"color":"red"})
print(a)

a.pop("color")
print(a)

a.popitem()
print(a)

del a["number"]
print(a)

a.clear()
print(a)

del a

print(a)

dict2 = {"brand": "ford",
         "brand": "ford",
          "electric": "false",
          "year":1964,
          "colors":["red","white","blue","red"]
          }
print(dict2)

for  x in dict2:
  print(x)

for  x in dict2:
  print(dict2[x])

for x in dict2.values():
  print(x)

for x in dict2.keys():
  print(x)

for x,y in dict2.items():
  print(x,":" ,y)

print(dict2 )

dict3 = dict2
print(dict3)

dict3["year"] = 2023
print(dict3)

print(dict2)

mydict = dict(dict3)
print(mydict)

dict4 = dict3.copy()
print(dict4)

dict4["year"]  = 2012
print(dict4)
print(dict3)

myfamily = {

            "child2" :{ "name":"durga","year" :2016},
            "child3" :{ "name":"vamsi",  "year" :2020}
             }

print(myfamily)

print(myfamily["child2"])

print(myfamily["child2"]["name"])

child2 = { "name":"durga","year" :2016}
child3 = { "name":"vamsi",  "year" :2020}

my_family = {"child2":child2,"child":child3}
print(my_family)

company = {
           "product" :{"cloths","mobiles","home-applie","electronict"},
           "discont":{20,30,15,10},
           "price": {1000,5000,2000,6000}

}
for x,y in company.items():
  print(x,y)

a = {"number" : {1,2,3},
     "mul of 2": {2,4,6}
     }
print(a)