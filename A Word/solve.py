def Corrected_word(word: str):
    lower_count = sum(1 for c in word if c.islower())
    upper_count = len(word) - lower_count  # Total length minus lowercase count gives uppercase count
    
    if upper_count > lower_count:
        print(word.upper())
    else:
        print(word.lower())
# Read input
word = input()

# Output
Corrected_word(word) 