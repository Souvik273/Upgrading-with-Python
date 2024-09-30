# -------------------------------Dictionaries in Python------------------------------
"""
    Dictionaries are powerful and commonly used data structures in Python for mapping keys to values efficiently.
    Dictionaries in Python are unordered collections of key-value pairs.
    They are mutable and versatile data structures used to store mappings of unique keys to values.
"""

# Creating Dictionaries
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing and Modifying Elements
print(my_dict['name'])   # Output: John
my_dict['age'] = 35      # Modify value associated with 'age'
my_dict['gender'] = 'Male'  # Add new key-value pair
del my_dict['city']      # Remove 'city' key and its associated value

# Dictionary Methods
print(my_dict.keys())     # Output: dict_keys(['name', 'age', 'gender'])
print(my_dict.values())   # Output: dict_values(['John', 35, 'Male'])
print(my_dict.items())    # Output: dict_items([('name', 'John'), ('age', 35), ('gender', 'Male')])

# Dictionary Comprehension
my_dict = {x: x**2 for x in range(1, 6)}
print(my_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Handling Missing Keys
print(my_dict.get('age'))      # Output: 35
print(my_dict.get('address'))  # Output: None (key not found)

# Dictionary Operations
print('name' in my_dict)  # Output: True
print(len(my_dict))       # Output: 5
my_dict.clear()           # Clear all items from the dictionary

# Dictionary Views
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys_view = my_dict.keys()
print(keys_view)         # Output: dict_keys(['a', 'b', 'c'])
my_dict['d'] = 4         # Update dictionary
print(keys_view)         # Output: dict_keys(['a', 'b', 'c', 'd']) (view reflects changes)
