# This program determines if a number is prime

# Input integer number and validate it is 2 or beyond.
number = int(input("Enter a number 2 or greater: "))
while number < 2:
    print("Invalid input.")
    number = int(input("Enter a number 2 or greater: "))

# Check if number is prime
isPrime = True
endTestValue = number//2 + 1
for testNumber in range(2, endTestValue):
    if number % testNumber == 0:
        isPrime = False

# Indicate if number is prime or not
print()
if isPrime == True:
    print(number,"is PRIME")
else:
    print(number,"NOT prime")



