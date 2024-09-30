# ---------------------------------------Arithmetic Operator ---------------------------
x = 9
y = 5

print(x+y)          # Addition
print(x-y)          # Subtraction
print(x*y)          # Multiplication
print(x/y)          # Division
print(x//y)         # Floor : eg :- floor(5.9) = 5 ; floor(-3.4) = -4
print(x%y)          # Modulo operator
print(x**y)         # Power x to the power of y

# precedence of operator :- " +,- " < "* / // " < " **"
print(5+3*4**2)

# Associativity is from left to right

# --------------------------------------Logical Operator ---------------------------
a=10
b=20
c=30
print(a<b and b<c)
print(a<b or b<c)
print(not a>b)

'''
Short-circuit : 
               for "or" operator if the first expression is true then it will not evaluate the second 
               for "and" operator if the first expression is false then it will not evaluate the second
               otherwise the second expression will be the result
'''

x = 0
print(x or 40)
y=10
print(y and 30)

# ---------------------------------Identity comparison operator----------------------------
# 'is' , 'is not' : These are two operator that check the id location are same or not

x1=10
x2=10
y1=10.5
y2=10.5
z1='Hello'
z2='Hello'
z3='10'

print(x1 is x2 )
print(y1 is y2)
print(z1 is z2)
print(x1 is z3)
print(x1 is not z3)

# When the value and the data types are same for two variables python doesn't allocate diff memory for them
# But for the Collections like list and tuples it is false even though they have same values

l1 = [10,20,30]
l2 = [10,20,30]
print(l1 is not l2)

# ---------------------------------Membership Operator -----------------------------------------
"""
    There are two membership operator : - 
        1. in       2. not in
    for string they check for substring
    for dictionary they check for key 
    list , set , tuple etc : check for membership 
"""
s = "Hello my followers"
print('followers' in s)

dict = {10:"Hello"}
print(10 in dict)
print('Hello' in dict)

l = [10,20,30]
print(10 in l)
print([20,30] in l)             # false as [20,30] is sublist not the member of list

# ------------------------------ Bitwise Operator --------------------

# using 'bin()' function we can convert any decimal to binary
# using 'int((val),base)' we can convert any val to decimal