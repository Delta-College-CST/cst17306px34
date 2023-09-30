# General a table of Celsius and Fahrenheit temperatures

print("  Celsius Fahrenheit")
for tempC in range(-40, 45, 5):
    tempF = 9.0 / 5.0 * tempC + 32.0
    print ("%7d  %7d" % (tempC, tempF))

