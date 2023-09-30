# This program builds a table to demonstrate compound interest
# accumulated for a bank investment.  Interest is compounded
# monthly

COMPOUNDS_PER_YEAR = 12

# Collect input on investment     
investAmount = float(input("Investment amount? "))
annualRate   = float(input("Annual interest rate (%)? "))
years        = int(input("Number of years? "))

# Initialize
totalCompoundings = years * COMPOUNDS_PER_YEAR
monthlyRate = annualRate / 12.0 / 100.0
balance = investAmount

# Writing headings
print("\n\n")
print("Month     Start       End")

# Generate report one month at a time for loan duration.
# Note retention of 'balance' as "old" balance, but at
# end of loop the "new" balance becomes the balance to
# set up for next iteration.
month = 0
while month < totalCompoundings:
    newBalance = balance + balance * monthlyRate
    month = month + 1
    print ("%3d    $%8.2f    $%8.2f" %(month, balance, newBalance))
    balance = newBalance


    



