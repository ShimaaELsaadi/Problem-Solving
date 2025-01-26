# Read the number of games played
n = int(input())

# Read the string representing the results of the games
Score = input()

# Initialize counters for Anton's and Danik's wins
A = 0  # Count of games won by Anton
D = 0  # Count of games won by Danik

# Iterate through each game result
for i in range(n):
    if Score[i] == 'A':  # Check if Anton won this game
        A += 1
    else:  # If not Anton, then Danik won this game
        D += 1

# Determine the overall winner or if it's a tie
if A == D:
    print('Friendship')  # Print "Friendship" if both won the same number of games
elif A < D:
    print('Danik')  # Print "Danik" if Danik won more games
else:
    print('Anton')  # Print "Anton" if Anton won more games
