# -----------------------------Substring in Python--------------------------------------

#A substring of a string s is any contiguous sequence of characters within s. This means that a substring is a part of the original string.


s = "Hello, World!"
substring1 = s[7:12]  # Characters from index 7 to 11 (12 is excluded)
print(substring1)  # Output: World

substring2 = s[:5]  # Characters from beginning to index 4 (5 is excluded)
print(substring2)  # Output: Hello

substring3 = s[7:]  # Characters from index 7 to the end
print(substring3)  # Output: World!
