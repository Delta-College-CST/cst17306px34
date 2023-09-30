# This program processes payroll for hourly workers

print("NAME    HOURS    PAY")          # Reporting heading

datafile = open("workerdata.txt", "r") # Open file for reading

# Initialize pay
totalPay = 0

# Perform file processing loop until end
for line in datafile:

    # Read one line of data - one worker
    name, hoursStr, rateStr = line.split(",")

    # Convert numeric strings to numbers
    hours = float(hoursStr)
    rate  = float(rateStr)

    # Determine pay, add to total, and write line of output
    pay     = hours * rate
    totalPay += pay
    print ("%-7s %3d   $%7.2f" %(name, hours, pay))

# Write total as report summary
print ("              $%7.2f" % (totalPay))


