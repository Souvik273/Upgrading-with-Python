#----------------------------------Function-------------------------------
def greet(name):
    """This function greets the person passed in as a parameter."""
    print("Hello, " + name + "!")
greet("Alice")  # Output: Hello, Alice!


# Return Statement
def square(x):
    """This function returns the square of the input."""
    return x * x

result = square(5)
print(result)  # Output: 25

# Multiple Parameter
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

print(add(3, 4))  # Output: 7


# Default Arguments
# You can provide default values for function parameters. These values are used if the function is called without the corresponding arguments.

def power(base, exponent=2):
    """Raise base to the power of exponent."""
    return base ** exponent

print(power(2))      # Output: 4 (2^2)
print(power(2, 3))   # Output: 8 (2^3)

# A function to check if a given number is prime:
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(17))  # Output: True
print(is_prime(21))  # Output: False


