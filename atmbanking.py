# This program creates a simple banking menu.  It assumes a
# $0 starting balance and allows a deposit or withdrawal.
# Withdrawals cannot exceed current balance.  A third option
# adds a 1% interest to the balance.

balance = 0.00           # Initial balance
INTEREST_RATE = 0.01     # Current interest rate for account
transactionOver = False  # To control continuation of transaction

while not transactionOver:

    # Display menu and accept menu selection
    print()
    print("BANK of DELTA")
    print("1: Deposit")
    print("2: Withdrawal")
    print("3: Add Interest")
    print("0: Quit")
    selection = int(input("Enter Selection: "))
    print()

    # Prepare to quit
    if selection == 0:
        print("Thank you for banking with us.")
        transactionOver = True

    # Manage deposit
    if selection == 1:
        amount = float(input("Enter amount to deposit: "))
        print("$",amount,"deposited")
        balance = balance + amount

    # Manage withdrawal
    if selection == 2:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Balance funds insufficient")
        else:
            print("$",amount,"withdrawn")
            balance = balance - amount

	# Manage interest increase
    if selection == 3:
            balance = balance + INTEREST_RATE * balance

    # For all valid user menu choicees, display balance.
    # If selection out of range, provide error message.
    if selection >= 0 and selection <= 3:
        print("Balance now: $%8.2f" % (balance))
    else:
        print("Invalid selection - try again")
				

