def determine_gender(username: str):
# Determine gender based on the number of distinct characters
    if len(set(username)) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

# Input
username = input()

# Output
determine_gender(username)