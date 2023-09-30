# This program prompts the user for an employee's work time
# and pay rate.  It determines the weekly gross pay considering
# time-and-a half for hours over the base 40 hour work week.

BASE_HOURS = 40.0
doAgain = True

while doAgain == True:
        
    # Prompt for worker input
    hoursWorked = float(input("Enter hours worked: "))
    payRate     = float(input("Enter pay rate: "))

    # Calculate gross pay for week
    if hoursWorked <= BASE_HOURS:
        pay = hoursWorked * payRate
    else:
        pay = hoursWorked * BASE_HOURS + (hoursWorked - BASE_HOURS) * 1.5 * payRate

    # Report payroll summary
    print ("PAYROLL")
    print ("Pay rate: $%6.2f per hour" % (payRate))
    print ("Hours Worked:",hoursWorked,"hours")
    print ("Paycheck: $%7.2f" % (pay))
    print()

    # Prompt for continuation
    response = input("Continue with another employee (y or n)?")
    if response == "Y" or response == "y":
        doAgain = True
    else:
        doAgain = False

