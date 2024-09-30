# ----------------------------------Tuples in Python--------------------------------
"""
    Tuples in Python are ordered, immutable collections of objects.
    They are similar to lists but cannot be modified once created.
"""

# Creating Tuples
my_tuple = (1, 2, 3, 4, 5)

# Accessing Elements
print(my_tuple[0])   # Output: 1
print(my_tuple[-1])  # Output: 5

# Slicing Tuple
print(my_tuple[1:3])   # Output: (2, 3)
print(my_tuple[::-1])  # Output: (5, 4, 3, 2, 1) (reversed tuple)

# Immutable Nature
# Attempting to modify a tuple will result in an error
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Tuple Packing and Unpacking
# Tuple packing
my_tuple = 1, 2, 3

# Tuple unpacking
x, y, z = my_tuple
print(x, y, z)  # Output: 1 2 3

# Tuple Methods
my_tuple = (1, 2, 2, 3, 4)
print(my_tuple.count(2))  # Output: 2 (number of occurrences of 2)
print(my_tuple.index(3))  # Output: 3 (index of the first occurrence of 3)

# Tuple Operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)