# This program writes the height as a function of time for
# a rocket flight.  The 

# Writing headings
print("\n\n")
print("  Time (s)  Height (m)")

# Generate table defining height of rocket as time varies
time = 0
height = 60
while height > 0:
    # Determine height for current time
    height = 60 + 2.13 * time**2 - 0.0013 * time**4 + 0.000034 * time**4.751

    # Write details of time/height for this iteration
    print ("%6.1f    %8.3f" %(time, height))

    # Increment for next calculation
    time += 2.0



