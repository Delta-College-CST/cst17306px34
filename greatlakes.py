# This map reads a file of raw mapping coordinate line segments
# to draw  map of the Great Lakes.

import turtle

pen = turtle.Turtle()
pen.speed(9)

# Files processing
datafile = open("mapdata.txt", "r") # Open file for reading

for mappoint in datafile:

    # Read one line of comma separated data - as strings
    x1str, y1str, x2str, y2str = mappoint.split(",")

    # Convert coordinates from str to float
    x1 = float(x1str)
    y1 = float(y1str)
    x2 = float(x2str)
    y2 = float(y2str)

    # Draw line segment
    pen.up()
    pen.goto(x1,y1)
    pen.down()
    pen.goto(x2,y2)


