# This program calculates miles per gallong   

# Loop through fill-ups
miles   = int(input ('Enter miles since last fill-up: '))
gallons = float(input ('Enter gallons added: '))

# Determine MPG and write output
mpg = float(miles) / gallons
print ('MPG: ', mpg)
    
