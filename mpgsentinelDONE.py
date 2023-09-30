# Sentinel-controlled loop to determine overall mileage
# for a trip with multiple fill-ups.  At each entry,
# inputs of miles driven and gallons used are read.  The
# inputs continue until either miles or gallons are zero

# Define accumulators
totalMiles   = 0      
totalGallons = 0      

# Loop through fill-ups
miles   = int(input ('Enter miles since last fill-up: '))
gallons = float(input ('Enter gallons added: '))
while miles > 0 and gallons > 0:
    totalMiles   = totalMiles + miles
    totalGallons = totalGallons + gallons
    miles   = int(input ('Enter miles since last fill-up: '))
    gallons = float(input ('Enter gallons added: '))

# Determine overall MPG and write output
mpg = float(totalMiles) / totalGallons
print ("MPG: %6.1f" % (mpg))
    
