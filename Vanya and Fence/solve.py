# Input number of heights (n) and the height limit (h)
n, h = map(int, input().split())
 
# Input all heights in a single line
hi = list(map(int, input().split()))
 
# Initialize total width
width = 0
 
# Process each height
for height in hi:
    if height <= h:
        width += 1
    else:
        width += 2
 
# Output the total width
print(width)