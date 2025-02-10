# Lexicographical String Comparison

## Problem Description
Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is, an uppercase letter is considered equivalent to the corresponding lowercase letter. Your task is to help Petya perform the comparison.You can find the original problem statement here: [Petya and Strings](https://codeforces.com/contest/112/problem/A)

## Input Format
- The first line contains a string `s1`.
- The second line contains a string `s2`.
- Both strings consist of uppercase and lowercase Latin letters and have the same length.

## Output Format
- Print `-1` if `s1` is lexicographically smaller than `s2`.
- Print `1` if `s1` is lexicographically greater than `s2`.
- Print `0` if `s1` and `s2` are equal (ignoring case).

## Constraints
- `1 ≤ |s1|, |s2| ≤ 100`
- Both strings have the same length.

## Solution Approach
- Convert both input strings to lowercase.
- Compare them lexicographically.
- Print the corresponding result based on the comparison.

## Example
### Input
```
hello
world
```
### Output
```
-1
```

## Implementation
Here is the Python implementation:
     [Solution](./solve.py)
## How to Run the Program
1. Clone the repository:
   ```sh
   git clone https://github.com/ShimaaELsaadi/Problem-Solving.git
   cd Petya and Strings
   ```
2. Run the script:
   ```sh
    python solve.py
   ```
3. Enter values for `s1` and `s2` when prompted.
## Complexity Analysis
- **Time Complexity**: O(n), where `n` is the length of the strings (since comparison takes linear time).
- **Space Complexity**: O(1), as only a few variables are used.

## License
 This project is licensed under the MIT License.

