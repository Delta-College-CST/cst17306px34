BASE_HOURS = 40.0

rate = float(input("Enter pay rate: "))
while rate <= 0:
    print("Pay rate invalid.")
    rate = float(input("Enter pay rate: "))

print ("\n")
print ("Hours    Pay")
for hours in range(5,65,5):
    if hours <= BASE_HOURS:
        pay = hours * rate
    else:
        pay = hours * BASE_HOURS + (hours - BASE_HOURS) * 1.5 * rate
    print("%3d   $%7.2f" % (hours,pay))
