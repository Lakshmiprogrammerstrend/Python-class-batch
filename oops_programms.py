# -*- coding: utf-8 -*-
"""OOPS Programms.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bRKRPSGQP3JI1xNx5OjCvS-kN-qLNTco

**1.Create a class Person with attributes name and age. Instantiate an object and print its details.**
"""

class person:
  def __init__(self,name,age):
    self.age = age
    self.name = name
  def __str__(self):
    return f"name: {self.name} \n age:{self.age}"

p1 = person("lakshmi",25)
print(p1)

class person:
  def __init__(self,name,age):
    self.age = age
    self.name = name
  def printname(self):
    return f"name: {self.name} \n age:{self.age}"

p1 = person("lakshmi",25)
print(p1)
print(p1.printname())

"""**2.Define a base class Shape with a method area. Create a subclass Circle that inherits from Shape and calculates the area.**"""

class shape:
  def area(self):
    pass

class circle(shape):
  def __init__(self,radius):
    self.radius = radius
  def area(self):
    return 3.14*self.radius**2

c1 = circle(4)

print(c1.area())

"""**3.Design a class Student with private attributes name and age. Provide methods to set and get these attributes.**"""

class student:
  def __init__(self,name,age):
    self.__name = name
    self.__age = age
  def set_name(self,name):
    self.__name = name
  def get_name(self):
    return self.__name
  def set_age(self,age):
    self.__age = age
  def get_age(self):
    return self.__age

s1 = student("lakshmi",15)

print(s1.get_name())
print(s1.get_age())


s1.set_name("durga")
s1.set_age(25)

print(s1.get_name())
print(s1.get_age())

"""**4.Create a class Animal with a method sound. Derive classes Dog and Cat that override the sound method.**"""

class animal:
  def sound(self):
    pass

class dog(animal):
  def sound(self):
    return "bowwwwww"
class cat(animal):
  def sound(self):
    return "meow"

dog1 = dog()
cat1 = cat()

print(dog1.sound())
print(cat1.sound())

"""**5.Design an abstract class Shape with an abstract method draw. Implement subclasses Circle and Square.**"""

from abc import ABC,abstractmethod
class shape(ABC):
  @abstractmethod
  def draw(self):
    pass

class circle(shape):
  def draw(self):
    print("drawing a circle")
class square(shape):
  def draw(self):
    print("drawing a square")


circle = circle()
square = square()

circle.draw()
square.draw()

"""**6. Create a class Calculator with methods for addition. Allow the add method to accept different numbers of arguments.**"""

class Calculator:
  def add(self,*arg):#** kwrag
    return sum(arg)

calc = Calculator()
result = calc.add(1,2,4,5,6)
print(result)

(l,k,*m) = ("apple","orange","banana","olive")
print(l)
print(k)
print(m)

"""**7.Define a class Vector and overload the + operator to perform vector addition.**"""

class vector:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __add__(self,other):
    return vector(self.x+other.x,self.y+other.y)

v1 = vector(1,2)
v2 = vector(3,4)
result = v1 + v2
print (result.x,result.y)

"""**8.Create a class MathOperations with a static method multiply to calculate the product of two numbers.**"""

class mathoperation:
  @staticmethod
  def multiply(a,b):
    return a*b

result = mathoperation.multiply(3,4)
print(result)

"""**9.Create a class Counter with a class variable count that keeps track of the number of instances created.**"""

class counter:
  count = 0
  def __init__(self):
    counter.count +=1

obj1 = counter()

obj2 = counter()

obj3 = counter()

obj4 = counter()

obj5 = counter()

print(counter.count)

"""**10.Design a class Employee with a class method from_string that creates an instance from a string representation.**"""

class Employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary
  @classmethod
  def from_strng(cls,employee_string):
    name,salary  = employee_string.split(",")
    return cls(name,int(salary))


emp_str = "john,50000"
emp1 = Employee.from_strng(emp_str)

print(emp1.name)
print(emp1.salary)

"""**11.Create classes A and B. Derive a class C from both A and B to demonstrate multiple inheritances.**"""

class A:
  def method_a(self):
    print('method  from class a')

class B:
  def method_b(self):
    print('method  from class b')


class C(A,B):
  pass


obj = C()

print(obj.method_a())
print(obj.method_b())