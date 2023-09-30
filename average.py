# Sentinel-controlled loop to calculate an average of a
# sequence of positive integers.  Program returns average
# and terminates after zero or negative number entered

total = 0      # Summation variable
count = 0      # Counting  variable

# Initiate averaging
number = int(input ('Enter a number: '))
while number > 0:
    total += number						
    count += 1
    number = int(input('Enter a number: '))

# Process average and report results
average = float(total) / float(count)
print ('Average: ', average)
    
