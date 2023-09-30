# This program prompts the user for an employee's pay rate.
# It determines the weekly gross pay for a range of hours considering
# time-and-a half for hours over the base 40 hour work week.

BASE_HOURS = 40.0

# Prompt for pay rate - validate it at positive
rate = float(input("Enter pay rate: "))
while rate <= 0:
    print("Pay rate invalid.")
    rate = float(input("Enter pay rate: "))

# Generate pay table for a range of hours
print ("\n")
print ("Hours    Pay")
for hours in range(5,65,5):
    
    if hours <= BASE_HOURS:
        pay = hours * rate
    else:
        pay = hours * BASE_HOURS + (hours - BASE_HOURS) * 1.5 * rate
        
    print("%3d   $%7.2f" % (hours,pay))
