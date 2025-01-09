import sys

# Get the number from command-line argument
n = int(sys.argv[1])

# Check if the number is even or odd
if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")
