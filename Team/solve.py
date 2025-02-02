# Read the number of problems
n = int(input())

# Initialize a counter for the number of problems to implement
contest = 0

# Loop through each problem
for _ in range(n):
    # Read the input for the current problem
    # Split the input into a list of strings and convert them to integers
    petya, vasya, tonya = map(int, input().split())
    
    # Check if at least two friends are confident
    if petya + vasya + tonya >= 2:
        contest += 1

# Print the total number of problems to implement
print(contest)