# Sentinel-controlled infinite while-loop using
# break operation to exit

sum = 0
count = 0

while True:
    value = int(input("Enter number:"))
    if value <= 0:
    	break
    sum   += value
    count += 1
    
average = float(sum) / float(count)
print("Average:",average)
print()

##################################################

# Perform a division as long as divisor is not zero.

num = int(input("Enter numerator:"))
den = int(input("Enter denominator:"))

if den == 0:
    pass
else:
    quotient = num / den
print()	

##################################################

# Write only values divisible by 3 from 0...100

for i in range(0,100):
    if i % 3 != 0:
        continue
    print(i)

##################################################

