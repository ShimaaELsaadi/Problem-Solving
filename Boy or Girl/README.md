# Determine Gender by Username

## Problem Description
Many boys use beautiful girls' photos as avatars in forums, making it difficult to determine a user's gender at first glance. To solve this problem, our hero has devised a method to identify a user's gender based on their username.

The method is as follows: If the number of distinct characters in a username is **odd**, the user is considered **male**; otherwise, the user is considered **female**.You can find the original problem statement here: [Boy or Girl](https://codeforces.com/contest/236/problem/A)

## Input Format
- A single non-empty string `username` consisting of **lowercase** English letters.
- The length of `username` does not exceed **100** characters.

## Output Format
- Print **"CHAT WITH HER!"** if the username has an **even** number of distinct characters.
- Print **"IGNORE HIM!"** if the username has an **odd** number of distinct characters.

## Constraints
- `1 ≤ |username| ≤ 100`
- The string contains only **lowercase** English letters.

## Solution Approach
- Convert the username into a **set** to extract distinct characters.
- Count the number of unique characters.
- If the count is **even**, print "CHAT WITH HER!"; otherwise, print "IGNORE HIM!".

## Example
### Input
```
wjmzbmr
```
### Output
```
CHAT WITH HER!
```

## Implementation
Here is the Python implementation:
     [Solution](./solve.py)
1. Clone the repository:
   ```sh
   git clone https://github.com/ShimaaELsaadi/Problem-Solving.git
   cd Boy or Girl
   ```
2. Run the script:
   ```sh
    python solve.py
   ```
3. Enter values for `username`.

## Complexity Analysis
- **Time Complexity**: O(n), where `n` is the length of the username (since converting to a set and checking length is linear).
- **Space Complexity**: O(1), as only a set is used to store distinct characters.

## License
This project is licensed under the MIT License.

