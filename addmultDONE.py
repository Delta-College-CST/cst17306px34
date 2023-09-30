# This program simulates multiplation using repetitive addition

# Input two integers (assuming positive)
a = int(input("Enter first positive number: "))
b = int(input("Enter second positive number: "))

# Repeat addition to simuate multiplication
product = 0
for n in range(a):
    product = product + b

# Output
print("Product of",a," * ",b,"=",product)


