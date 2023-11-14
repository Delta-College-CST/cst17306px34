# This program simulates throwing a die 6000
# times to count frequency of each face

import random

NUM_THROWS = 6000

# Initilize counting variables
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

# Begin simulation.  Loop to throw doe
# each occurrence of each face.
for count in range (1,NUM_THROWS+1):
    dieThrow = random.randint(1,6)
    if dieThrow == 1:
        num1 = num1 + 1
    if dieThrow == 2:
        num2 = num2 + 1
    if dieThrow == 3:
        num3 = num3 + 1
    if dieThrow == 4:
        num4 = num4 + 1
    if dieThrow == 5:
        num5 = num5 + 1
    if dieThrow == 6:
        num6 = num6 + 1
        
# Summarize the simulation
print("For",NUM_THROWS,"throws: ")
print("1:",num1)
print("2:",num2)
print("3:",num3)
print("4:",num4)
print("5:",num5)
print("6:",num6)
