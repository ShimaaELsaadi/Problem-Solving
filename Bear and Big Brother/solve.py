# Read input and split into two integers: Limak's weight (a) and Bob's weight (b)
weight = input().split()

# Convert input values from strings to integers
a = int(weight[0])  # Limak's initial weight
b = int(weight[1])  # Bob's initial weight

# Initialize a counter for the number of years
y = 0

# Loop until Limak's weight becomes strictly greater than Bob's weight
while a <= b:
    y += 1  # Increment year count
    a *= 3  # Limak's weight triples each year
    b *= 2  # Bob's weight doubles each year

# Print the total number of years required for Limak to become strictly heavier than Bob
print(y)