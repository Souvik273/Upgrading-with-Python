# ------------------------------------String---------------------------------
"""
    Strings are fundamental data types in Python, used extensively for representing text-based information and manipulating textual data.
    Strings in Python are sequences of characters, enclosed within either single quotes (') or double quotes (").
    They are immutable, meaning they cannot be changed after creation.
"""

'''Creating Strings
You can create a string in Python by enclosing characters within quotes.

Example:'''
my_string = "Hello, World!"

'''2. Accessing Characters
You can access individual characters of a string using index notation. Indexing starts from 0 for the first character and can also be negative to count backward from the end.

Example:'''
print(my_string[0])   # Output: H
print(my_string[-1])  # Output: !


'''3. Slicing Strings
You can extract a portion of a string using slicing notation start:end:step. Omitting start and end defaults to the beginning and end of the string, respectively. Negative indices can also be used.

Example:'''
print(my_string[1:5])   # Output: ello
print(my_string[::-1])  # Output: !dlroW ,olleH (reversed string)


'''4. String Concatenation
Strings in Python can be concatenated using the + operator.

Example:'''
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # Output: Hello, Alice!


'''5. String Methods
Python provides numerous built-in methods for working with strings, such as upper(), lower(), strip(), split(), join(), replace(), find(), count(), and many more.

Example:'''


my_string = "    Hello, World!    "
print(my_string.strip())      # Output: "Hello, World!"
print(my_string.lower())      # Output: "hello, world!"
print(my_string.split(", "))  # Output: ['Hello', 'World!']


'''6. String Formatting
Python supports multiple ways of formatting strings, including using the % operator, the str.format() method, and f-strings (formatted string literals).

Example:'''


name = "Alice"
age = 30
print("Name: %s, Age: %d" % (name, age))  # Output: Name: Alice, Age: 30
print("Name: {}, Age: {}".format(name, age))  # Output: Name: Alice, Age: 30
print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 30


'''7. String Escape Sequences
Escape sequences allow you to include special characters in strings, such as newline (\n), tab (\t), and backslash (\\).

Example:'''


escaped_string = "This is a new line\nThis is a tab\tThis is a backslash: \\"
print(escaped_string)


'''8. String Operations
Python supports various operations on strings, such as repetition (*), membership (in), and length (len()).

Example:'''


string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print(concatenated_string)  # Output: Hello World