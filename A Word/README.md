# A. Word

## Problem Statement
Vasya dislikes seeing words with mixed uppercase and lowercase letters. To fix this, he decided to develop a browser extension that modifies each word to be either fully lowercase or fully uppercase, with minimal letter changes.

A given word should be transformed based on the following rules:
- If there are more uppercase letters than lowercase letters, convert the word to uppercase.
- Otherwise, convert the word to lowercase.
- If the number of uppercase and lowercase letters is equal, convert the word to lowercase.

You can find the original problem statement here: [A Word](https://codeforces.com/contest/59/problem/A)

## Input Format
- A single word `word` consisting of uppercase and lowercase Latin letters.
- The length of `word` is between `1` and `100`.

## Output Format
- Print the transformed word following the specified rules.

## Constraints
- `1 ≤ |word| ≤ 100`  (where `|word|` is the length of `word`).

## Examples
### Example 1
#### Input:
```
HoUse
```
#### Output:
```
house
```
### Example 2
#### Input:
```
ViP
```
#### Output:
```
VIP
```
### Example 3
#### Input:
```
maTRIx
```
#### Output:
```
matrix
```

## Solution Approach

The solution determines the number of uppercase and lowercase letters in the word. If uppercase letters outnumber lowercase letters, the word is converted to uppercase; otherwise, it is converted to lowercase.

## Code Implementation
Here is the Python implementation:
     [Solution](./solve.py)

## Explanation of the Code
1. **Count lowercase letters** using `sum(1 for c in word if c.islower())`.
2. **Calculate uppercase letters** by subtracting the lowercase count from the total length.
3. **Determine the correct transformation**:
   - If uppercase letters are more, convert the word to uppercase.
   - Otherwise, convert the word to lowercase.
4. **Read input** and print the transformed word.

## Repository Structure
```
/ (Root Directory)
│-- README.md  # Documentation
│-- solve.py  # Python solution file
```

## How to Run the Program
1. Clone the repository:
   ```sh
   git clone https://github.com/ShimaaELsaadi/Problem-Solving.git
   cd A Word
   ```
2. Run the script:
   ```sh
   python solve.py
   ```
3. Enter the input when prompted and check the output.

## Contributing
Feel free to open an issue or submit a pull request if you find any improvements!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

