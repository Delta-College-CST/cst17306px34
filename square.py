# This program demonstrates nested loops
# by building a "square" of characters with
# size dictated by the user.

# Input and validation
size = int(input("Enter size of square (1-12): "))
while size < 1 or size > 12:
    print("Error - Size must be 1..12")
    size = int(input("Please re-enter: "))

# Generate square
print()
for num in range (1,size+1):
    for i in range (1,size+1):
        print("#", end="")
    print()
