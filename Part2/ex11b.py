# TODO:
# Create a function called calculate that takes three arguments:
# - A number
# - An operator ("+", "-", "*", or "/")
# - Another number
# The function should return the result of the calculation

# Insert your function code here
def calculate(n1, o, n2):
    if o == ("+"):
        return (float(n1 + n2))
    if o == ("-"):
        return (float(n1 - n2))
    if o == ("*"):
        return (float(n1 * n2))
    if o == ("/"):
        return (float(n1 / n2))

# Test the function with different operations
print(calculate(10, "+", 10))  # should return 20
print(calculate(10, "-", 10))  # should return 0
print(calculate(10, "*", 10))  # should return 100
print(calculate(10, "/", 10))  # should return 1.0