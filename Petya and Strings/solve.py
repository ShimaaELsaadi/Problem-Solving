def compare_strings(s1: str, s2: str) -> int:
    # Compare the strings lexicographically
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0

# Input and Convert both strings to lowercase for case-insensitive comparison

s1 = input().lower()
s2 = input().lower()

# Output
print(compare_strings(s1, s2))