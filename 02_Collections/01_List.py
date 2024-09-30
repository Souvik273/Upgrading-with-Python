# -------------------------------List----------------------------------------------
"""
    It is ordered , mutable , and Collection of Objects
    They can contain different data structure also a list
"""
# Creating a list
my_list = [1,2,3,4,5]
print(type(my_list))

# Accessing element
print(my_list[0])
print(my_list[-1])

# slicing list : list[start:end:step]       ;- Excluding start , end
print(my_list[1:3])
print(my_list[::-1])            # reversing the list

# Modifying list
my_list[0] = 10
print(my_list)
my_list.append(6)
print(my_list)


# List Methods
my_list.append(7)                           # Append 7 to the end
my_list.extend([8, 9])                      # Extend with another list
my_list.insert(2, 11)        # Insert 11 at index 2
my_list.remove(5)                           # Remove the first occurrence of 5
my_list.pop(3)                              # Remove and return the element at index 3
print(my_list)                              # Output: [10, 2, 11, 4, 6, 7, 8, 9]


#  List Comprehensions
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Nested Lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][0])  # Output: 4 (accessing element in nested list)

# List Operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]
