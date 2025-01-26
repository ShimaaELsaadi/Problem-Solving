# Vanya and Fence (Codeforces Problem 677A)

This repository contains the solution to Codeforces Problem 677A, "Vanya and Fence."

## Problem Statement

Vanya and his friends are walking along the fence that is `h` units high. Each friend can pass through the fence either:

- Without bending, if their height is less than or equal to `h`, or
- By bending down, which takes twice the space as passing without bending.

The goal is to calculate the total width required for all friends to pass the fence.

You can find the original problem statement here: [Vanya and Fence](https://codeforces.com/contest/677/problem/A)

---

## Input Format

1. The first line contains two integers:

   - `n` (1 <= n <= 1000): The number of friends.
   - `h` (1 <= h <= 1000): The height of the fence.

2. The second line contains `n` integers:

   - Each integer represents the height of a friend (1 <= height <= 2000).

---

## Output Format

Output a single integer, the total width required for all friends to pass the fence.

---

## Example

### Input:

```
3 7
4 5 14
```

### Output:

```
4
```

### Explanation:

- Friend 1 has height `4` and can pass without bending (width = 1).
- Friend 2 has height `5` and can also pass without bending (width = 1).
- Friend 3 has height `14` and must bend down (width = 2).

Total width = 1 + 1 + 2 = 4.

---

## Solution

### Approach:

1. Read `n` and `h` from input.
2. Read the list of heights of friends.
3. For each friend's height:
   - Add `1` to the total width if the height is less than or equal to `h`.
   - Add `2` to the total width otherwise.
4. Print the total width.

### Implementation:
Solution here >> [Solution](./solve.py)

## Complexity

### Time Complexity:

- **O(n)**: We iterate through the list of heights once.

### Space Complexity:

- **O(1)**: We use constant additional space.

---

## Testing

### Test Case 1:

Input:

```
3 7
4 5 14
```

Output:

```
4
```

### Test Case 2:

Input:

```
5 6
1 2 3 7 8
```

Output:

```
7
```

### Test Case 3:

Input:

```
4 10
11 10 9 12
```

Output:

```
6
```

---

## Notes

- This problem is straightforward with a simple loop and conditional logic.
- It demonstrates basic input/output handling and decision-making in programming.

---

## Repository Structure

```
/
├── README.md         # Problem explanation and solution details
├── solve.py          # Python implementation of the solution
└── test_cases.txt    # Sample input and output test cases
```

---

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/vanya-and-fence.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd vanya-and-fence
   ```

3. Run the solution:

   ```bash
   python solution.py
   ```

4. Provide input as per the format described above.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

