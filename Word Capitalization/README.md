# A. Word Capitalization

## Problem Statement

Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

Note that during capitalization, all letters except the first one remain unchanged.  
You can find the original problem statement here: [Word Capitalization](https://codeforces.com/contest/281/problem/A)


## Input Format

- A single line contains a non-empty word.
- This word consists of lowercase and uppercase English letters.
- The length of the word will not exceed `1000`.

## Output Format

- Output the given word after capitalization.

## Constraints

- `1 ≤ |word| ≤ 103` (where `|word|` is the length of `word`).

## Examples

### Example 1

#### Input:

```
apple
```

#### Output:

```
Apple
```

### Example 2

#### Input:

```
HELLO
```

#### Output:

```
HELLO
```

### Example 3

#### Input:

```
javaScript
```

#### Output:

```
JavaScript
```

## Solution Approach

To solve this problem, we need to capitalize only the first letter of the given word while keeping the rest of the letters unchanged.

## Code Implementation
Here is the Python implementation:
     [Solution](./solve.py)

## Explanation of the Code

1. **Extract the first character** and convert it to uppercase using `word[0].upper()`.
2. **Concatenate it with the remaining substring** `word[1:]`.
3. **Print the result**, ensuring the first letter is capitalized while the rest remains unchanged.
4. **Read input** and process it accordingly.

## Repository Structure

```
/ (Root Directory)
│-- README.md  # Documentation
│-- solution.py  # Python solution file
```

## How to Run the Program
1. Clone the repository:
   ```sh
   git clone https://github.com/ShimaaELsaadi/Problem-Solving.git
   cd Word Capitalization
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


