# -*- coding: utf-8 -*-
"""FUNCTION .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dEiqYfNddS3684rNTp9QMZdFSTO2j1iR
"""

def myfunction():
  print("hello")
myfunction()

def my_function(fname):#parameter
  print(fname + "dodda")
my_function("lakshmi")#arg

def my_function(fname):#parameter
  print( "dodda"+fname)
my_function("lakshmi")#arg

def my_function(fname,lname):#parameter
  print( fname + lname)
my_function("lakshmi","dodda")#arg

def my_function(fname,lname):#parameter
  print( fname + lname)
my_function("lakshmi")#arg

def my_function(fname,lname):#parameter
  print(  lname + fname )
my_function("lakshmi","dodda")#arg

def my_function(fname,lname):#parameter
  print(  lname + fname )
my_function(fname ="lakshmi",lname = "dodda")#arg

def my_function(*fname):#parameter
  print(fname[1] )
my_function("lakshmi","dodda")#*arg

"""my_function("lakshmi","dodda")#*arg

my_function(fname ="lakshmi",lname = "dodda")#**kwarg
"""

def my_function(**kid):#parameter
  print(kid["lname"] )
my_function(fname ="lakshmi",lname = "dodda")#**kwarg

def my_country(country = "india"):
  print( " I am From "+ country)
my_country("sweden")
my_country("brazil")
my_country()
my_country("norway")

def sum_number(a,b,c):
  print(a+b+c)
sum_number(3,b=2,c=10)

def sum_number(a,b,c):
  print(a+b+c)
sum_number(3,a=2,b=10)

def my_food(food):#["apple","banana","orange"]
  for x in food:
    print(x)
fruits = ["apple","banana","orange"]
my_food(fruits)

def my_value(x):
  print(x)
  return 5*x
my_value(5)

def hello():
  pass

# find the maximu of three numbers
def find_max(a,b,c):
  max_number = max(a,b,c)
  return max_number

num1 = float(input("enter 1st number:"))
num2 = float(input("enter 2nd number:"))
num3 = float(input("enter 3rd number:"))

maximum = find_max(num1,num2,num3)

print(f"the maximum number is  {maximum} ")

#Factorial number
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
result = factorial(5)
print(result)

#Factorial number
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
for i in range(1,6):
  result = factorial(i)
  print(f"factorial of {i}  is {result}")

def pattren(item):#[2,3,6,5]
  for n in item:
    output = " "
    times = n#2
    while(times>0):#2
      output += "@"# output = output +"@"   @@
      times = times - 1
    print(output)
pattren([2,3,6,5])

#write a python program to find the total number of even or odd divisors of a given Integer
from IPython.terminal.interactiveshell import Integer
n = inter
0 to n
n%n


15 = 1,3,5,15(1to 15)#4
n%i = 0