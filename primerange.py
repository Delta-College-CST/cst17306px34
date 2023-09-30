# This program determines the first 100 prime nmbers

PRIME_COUNT = 100

count  = 0      # Will increment when a prim is detected
number = 2      # Number to test for prime - start at 2

for number in range(2000,3001):

    # Check if number is prime
    isPrime = True
    endTestValue = number//2+1
    
    for testNumber in range(2, endTestValue):
        if number % testNumber == 0:
            isPrime = False

    # If prime, increment prime count and write number
    if isPrime == True:
        count = count + 1

print("Primes between 2000 and 3000:", count)

