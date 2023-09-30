# This program reads a sequence of gas fill-up data including
# miles driven and gallons used.  It accumulates the file data and 
# calculates mileage data summarizing it in a tabular report.

print("CITY                     MPG")  # Heading

datafile = open("fillups.txt", "r") # Open file for reading

# Initialize accumulators
totalMiles   = 0
totalGallons = 0

# Perform file processing loop until end
for inputline in datafile:

    # Read one line of data - one trip segment
    city, milesStr, gallonsStr  = inputline.split(",")

    # Convert numeric strings to numbers
    miles    = float(milesStr)
    gallons  = float(gallonsStr)

    # Process line of data and write info for one fill-up
    mpg =  miles / gallons
    print ("%-18s   %7.1f" % (city, mpg))

    # Add trip segment to totals
    totalMiles   += miles
    totalGallons += gallons

# Summarize mileage for entire trip and display
overallMPG = totalMiles / totalGallons
print ("             OVERALL:%7.1f" % (overallMPG))

