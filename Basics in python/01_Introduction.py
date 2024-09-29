# -----------------------------------------Python-----------------------------------------

# Python is a widely used general-purpose, high-level programming language.
# It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation.

# ------------------------------------Taking input -----------------------------------------

# Syntax : inp = input('STATEMENT')
# Python program showing
# a use of input()

val = input("Enter your value: ")
print(val)

# Program to check input
# type in Python

num = input("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)

# Printing type of input value
print("type of number", type(num))
print("type of name", type(name1))

# Python program to take multiple integer input in one line in Python

a,b,c,d = map(int , input("Enter the four numbers:").split())
print(a,b,c,d)

# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map, split and strip functions
lst = list(map(int, input(
    "Enter the integer elements of list(Space-Separated): ").strip().split()))[:n]
print('The list is:', lst)  # printing the list


# ---------------------------------Type in Python ---------------------------------------------

a = ("Geeks", "for", "Geeks")
b = ["Geeks", "for", "Geeks"]
c = {"Geeks": 1, "for": 2, "Geeks": 3}
d = "Hello World"
e = 10.23
f = 11.22

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
# -----------------------------------------IS ----------------------------------------
print(type([]) is list)

print(type([]) is not list)

print(type(()) is tuple)

print(type({}) is dict)

print(type({}) is not list)
