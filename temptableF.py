# General a table of Fahrenheit and Celsius temperatures

print(" Fahrenheit Celsius ")
for tempF in range(-40, 120, 5):
    tempC = 5.0 / 9.0 * (tempF - 32.0)
    print ("%7d  %7d" % (tempF, tempC))

