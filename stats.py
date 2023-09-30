# This program performs a statistical analysis of a
# set of positive integer values.

FILENAME = "data.txt"

# Open file for reading
datafile = open(FILENAME, "r") 

sum = 0        # Summation variable
count = 0      # Counting  variable
max = -999999  # Set max to extremely low value
min = 999999   # Set min to extremely high value

# Perform file processing loop until end
for newDataStr in datafile:
    newData = int(newDataStr)   # Convert data str --> int
    sum = sum + newData         # Accumuate
    count = count + 1           # Count
    if newData > max:           # Test for maximum
        max = newData
    if newData < min:           # Test for minimum
        min = newData

# Summarize and display resulting statistical analysis
print("Dataset: ", FILENAME)
average = float(sum) / float(count)
print("Count:",count)
print ("Average: %6.2f" % average)
print("Max:", max)
print("Min:", min)

datafile.close()      # Close input file
