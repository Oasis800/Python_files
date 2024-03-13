"""
A program that uses the input
function to read two numbers
fromm the user and then adds
and later swaps the two numbers
"""
result = 0
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print(num1)
print(num2)
#type cast the string to int
num1 = int(num1)
num2 = int(num2)
result = num1 + num2
print("Sum of ",num1, "and ", num2, "gives:", result)
#swap num1 and num2 values
swap = num1
num1 = num2
num2 = swap
print(num1)
print(num2)
