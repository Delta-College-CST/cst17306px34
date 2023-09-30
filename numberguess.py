# This program plays a number guessing game.  The user is
# prompted to guess a number 1..100.  The program responds
# with hints.  The number of guesses required is accumulated
# and reported at the end.

import random

# Set the number and boolean for game control
theNumber = random.randrange(101)
gameOver = False

# Guess processing loop
guess = int(input("Guess a number 1..100: "))  # First user guess
count = 1                                      # Count 1st guess

while gameOver == False:
    if guess == theNumber:
        print ("Your guessed it!  It took",count,"tries")
        gameOver = True
    else:
        if guess < theNumber:
            print ("Too Low")
        else:
            print ("Too High")

        # Prompt the user to continue guessing; count guesses    
        guess = int(input("Guess a number 1..100: "))
        count = count + 1
        
