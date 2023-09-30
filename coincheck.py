# This program simulates flipping a coin 100 times
# to count frequency of heads or tails

import random

NUM_FLIPS = 100

numHeads = 0   # Count heads (tails derived from this)

# Begin simulation.  Loop to flip coins and count
# each occurrence of a "heads".
for count in range (1,NUM_FLIPS+1):
    coin = random.randint(0,1)
    if coin == 1:
        numHeads = numHeads + 1

# Summarize
numTails = NUM_FLIPS - numHeads

print("For",NUM_FLIPS,"throws: ")
print("Heads:",numHeads)
print("Tails:",numTails)

