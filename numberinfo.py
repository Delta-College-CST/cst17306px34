# This program generates integer values for a range 1..20
# (determined by the user).  It then displays the square,
# cube, and square root of the values.
import math

# Prompt user for input range value.  Validate it.
numRange = int(input("  Enter ending number 1..20: "))
while numRange < 1 or numRange > 20:
    print()
    print("Invalid input - Must be 1..20")
    numRange = int(input("  Enter ending number 1..20: "))

# Given valid table range, generate number analysis
print("Number  Square   Cube  Square Root")
for num in range(1,numRange+1):
    square = num * num
    cube   = num ** 3
    sqRoot = math.sqrt(num)
    print ("  %2d %7d %7d   %7.4f" % (num, square, cube, sqRoot))
