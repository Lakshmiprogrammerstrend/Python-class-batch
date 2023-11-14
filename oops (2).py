# -*- coding: utf-8 -*-
"""OOPS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rn0XWImMsM3A1ikm_SdiulcIbQUWaRrg

##OOPS

OOP, or Object-Oriented Programming, is a coding approach using objects (data structures with fields and methods) to create programs. Key principles are:

1. Encapsulation:Grouping data and methods into classes, acting as a blueprint.

2. Inheritance:Allowing a class to inherit properties from another, promoting code reuse.

3. Polymorphism: Treating different objects as if they belong to a common class, enhancing code flexibility.

4. Abstraction: Simplifying complex systems by focusing on essential properties and behaviors.


**Class:**

A class is like a blueprint. It defines the structure and behaviors that objects will have but doesn't represent a specific thing.

**Object:**

An object is like a thing created from the blueprint. It has specific characteristics and can perform actions based on what the blueprint (class) defines.

#Create a Class
"""

class myclass:
  x = 5

"""#Create Object"""

p1 = myclass()
print(p1.x)

"""#The __init__() Function

which is always executed when the class is being initiated.Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
"""

class car:
  def __init__(self,make,model,year,color):
    self.make = make
    self.model = model
    self.year = year
    self.color = color

car1 = car(2007,"audi",2010,"black")

print(car1.color)

print(car1.model)

car2 = car(2010,"tayota",2015,"white")
print(car2.make)

print(car2)

"""#The __str__() Function
The __str__() function controls what should be returned when the class object is represented as a string.
"""

class car:
  def __init__(self,model,year,color):
    self.model = model
    self.year = year
    self.color = color
  def __str__(self):
    return f"model = {self.model} \n year = {self.year} \n color = {self.color}"

car1 = car("audi",2013,"red")

print(car1)

"""#Object Methods

Objects can also contain methods. Methods in objects are functions that belong to the object.
"""

class car:
  def __init__(self,model,year,color):
    self.model = model
    self.year = year
    self.color = color
    self.speed = 0
  def __str__(self):
    return f"model = {self.model} \n year = {self.year} \n color = {self.color}"
  def accelerate(self):
    self.speed+=10
    print(f"the {self.year} {self.model} is accelerating speed: {self.speed}mph")

car1 = car("audi",2013,"red")

car1.accelerate()

"""#self Parameter

The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
"""

class this:
  def __init__(myjob,name,age):
    myjob.name = name
    myjob.age = age
  def details(myjob):
    return f"name = {myjob.name} \n age = {myjob.age}"
p1 = this("lakshmi",27)
p1.details()

"""#Modify Object Properties"""

class this:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def details(self):
    return f"name = {self.name} \n age = {self.age}"
p1 = this("lakshmi",27)
p1.age = 25
print(p1.age)

p1.name = "ram"
print(p1.name)

"""#Delete Object Properties"""

del p1.age
print(p1.age)

p2 = this("lakshmi",27)
print(p2.name)
print(p2.age)

"""#Delete Objects"""

del p1

print(p1.name)

"""#The pass Statement"""

class person:
  pass

"""#Encapsulation"""

class car:
  def __init__(self,make,model):
    self.make = make
    self.model = model
    self.speed = 0
  def accelerate(self):
    self.speed+=10
    print(self.speed)
  def brake(self):
    self.speed -=5
    print(self.speed)

car1 = car(2019,"audi")

car1.accelerate()

car1.brake()

"""#Inheritance"""

class parant:
  def __init__(self,fname,lname):
    self.firstname = fname
    self.lastname = lname
    self.speed = 0
  def printname(self):
      print(self.firstname,self.lastname)

y = parant("lakshmi","dodda")
y.printname()

class child(parant):
    def __init__(self, fname, lname):
      parant.__init__(self,fname, lname)

x = child("dodda","lakshmi")
x.printname()

class A:
  def method1(self):
    print("print A method1")
  def method2(self):
    print("print A method2")

class B(A):
  def method1(self):
    print("print B  method1")

class C(A):
  def method1(self):
    print("print C  method1")


class D(B,C):
   def method1(self):
    print("print D  method1")


d = D()

d.method1()

d.method2()

C.method1(d)

B.method1(d)

"""#Polymorphism"""

class car:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model
  def move(self):
    print("drive")
class boat:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model
  def move(self):
    print("sail")
class plane:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model
  def move(self):
    print("fly")

car1 = car("ford","mustang")#car class instance
boat1 = boat("ibiza","touring20")#boat class instance
plane1 = plane("boeing","747") # plane class instance


for i in (car1,boat1,plane1):
  i.move()

"""#inheritance in polymorphism"""

class vehical:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model
  def move(self):
    print("movie")
class car(vehical):
  pass

class boat(vehical):
  def move(self):
    print("sail")

class plane(vehical):
  def move(self):
    print("fly")

car1 = car("ford","mustang")#car class instance
boat1 = boat("ibiza","touring20")#boat class instance
plane1 = plane("boeing","747") # plane class instance


for x in (car1,boat1,plane1):
  print(x.brand)
  print(x.model)
  x.move()

"""#Abstraction"""

from abc import ABC,abstractmethod
class Account(ABC):
  def __init__(self,holder,balance=0):
    self.holder = holder
    self.balance = balance

  @abstractmethod
  def transact(self,amount):
    pass
class SavingSAccount(Account):
  def transact(self,amount):
    self.balance = self.balance+ amount#1000+500=1500
    return f"Transaction: +${amount} Newbalance:${self.balance} "
class checkingAcount(Account):
  def transact(self,amount):
    if amount>self.balance:
      return "insufficient funds for  withdrawal"
    else:
      self.balance = self.balance- amount
      return f"Transaction: -${amount} Newbalance:${self.balance}"#1500-500=1000


def interact(account,amount):
      print(account.transact(amount))

savings,checking = SavingSAccount("lakshmi",1000),checkingAcount("durga",1500)
interact(savings,500)
interact(checking,500)

