# This program averages a list of positive integer values
# stored in an external data file.

datafile = open("data.txt", "r") # Open file for reading

sum = 0        # Summation variable
count = 0      # Counting  variable

# Perform file processing loop until end
for newDataStr in datafile:
    newData = int(newDataStr)   # Convert data str --> int
    sum = sum + newData         # Accumuate
    count = count + 1           # Count

# Summarize and display average
average = float(sum) / float(count)
print("Average:",average)

datafile.close()      # Close input file
