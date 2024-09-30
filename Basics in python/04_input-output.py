# ---------------------------------Output--------------------------------------
print('Hello this is a python course')

print('Hello','We are upgrading')

# end is used to define how the end will be by default it is new line
print('Hello' , end='-')
print('World')

# sep is used to seperate the output
print('20','09','2024',sep='-')

# Python program showing
# use of format() method

# using format() method
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))

# using format() method and referring
# a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))

print('{1} and {0}'.format('Geeks', 'Portal'))


# the above formatting can also be done by using f-Strings
# Although, this features work only with python 3.6 or above.

print(f"I love {'Geeks'} for \"{'Geeks'}!\"")

# using format() method and referring
# a position of the object
print(f"{'Geeks'} and {'Portal'}")



# --------------------------------Input ---------------------------------

# Python program showing
# a use of input()

val = input("Enter your value: ")
print(val)

name = input('What is your name?\n')     # \n ---> newline  ---> It causes a line break
print(name)

# Program to check input
# type in Python

num = input ("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)

# Printing type of input value
print ("type of number", type(num))
print ("type of name", type(name1))


# Example : Sum of two number

a = int(input('Enter the first number :'))
b = int(input('Enter the second number:-'))
print(a+b)