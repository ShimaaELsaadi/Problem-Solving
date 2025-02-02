# Programming Contest Problem Solver

This Python script helps three friends—Petya, Vasya, and Tonya—decide how many programming contest problems they will solve based on their confidence in the solutions. The friends will implement a problem if at least two of them are confident about the solution.

---

## Table of Contents
1. [Problem Description](#problem-description)
2. [How It Works](#how-it-works)
3. [Usage](#usage)
4. [Example](#example)
5. [Contributing](#contributing)
6. [License](#license)

---

## Problem Description

During a programming contest, participants are given `n` problems. For each problem, the three friends indicate whether they are confident about the solution (`1` for confident, `0` for not confident). The friends will solve a problem if at least two of them are confident about the solution.
You can find the original problem statement here: [Team](https://codeforces.com/contest/231/problem/A)

### Input
- The first line contains an integer `n` (1 ≤ `n` ≤ 1000), the number of problems.
- The next `n` lines contain three integers each (`0` or `1`), representing the confidence of Petya, Vasya, and Tonya, respectively.

### Output
- A single integer representing the number of problems the friends will solve.

---

## How It Works

The [script](./solve.py) reads the number of problems and then iterates through each problem. For each problem, it checks how many friends are confident about the solution. If at least two friends are confident, the problem is counted as one they will solve. Finally, the total count of such problems is printed.

---

## Usage

1. Clone the repository:
   ```bash
        git clone https://github.com/ShimaaELsaadi/Problem-Solving.git
        cd Team
    ```
2. Run the script:
   ```bash
        python solve.py
    ```
3. Provide input as described in the [Problem Description](#problem-description)

---

## Examble
### Input:
   ```bash
        3
        1 1 0
        1 0 0
        0 1 1
   ```
### Output:
   ```bash
        2
   ```
### Explanation:
1. For the first problem, Petya and Vasya are confident, so it is counted.
2. For the second problem, only Petya is confident, so it is not counted.
3. For the third problem, Vasya and Tonya are confident, so it is counted.
4. The total number of problems to solve is 2.

---

## Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/YourFeature).
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
