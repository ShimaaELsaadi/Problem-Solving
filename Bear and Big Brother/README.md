# Limak vs Bob Weight Growth Problem

## Problem Statement
Bear Limak wants to become the largest of bears, or at least become larger than his brother Bob.

Initially, Limak and Bob weigh `a` and `b` respectively. It's guaranteed that Limak's weight is **less than or equal to** Bob's weight.

- Limak's weight **triples** each year.
- Bob's weight **doubles** each year.

The goal is to determine **how many full years it will take for Limak to become strictly heavier than Bob**.
You can find the original problem statement here: [Limak vs Bob Weight](https://codeforces.com/contest/791/problem/A)

## Input Format
- The input consists of a **single line** containing two integers `a` and `b`:
  - `1 ≤ a ≤ b ≤ 10`

## Output Format
- The program should output **one integer** denoting the number of years after which Limak will become strictly heavier than Bob.

## Example Runs
### **Example 1**
#### **Input:**
```
4 7
```
#### **Execution:**
```
Year 0: a = 4, b = 7
Year 1: a = 12, b = 14
Year 2: a = 36, b = 28  ✅ (Limak > Bob)
```
#### **Output:**
```
2
```

### **Example 2**
#### **Input:**
```
3 6
```
#### **Output:**
```
3
```
## Repository Structure

```
/
├── README.md         # Problem explanation and solution details
├── solve.py          # Python implementation of the solution
```

---

## Implementation
Here is the Python implementation:
     [Solution](./solve.py)

## How to Run the Program
1. Clone the repository:
   ```sh
   git clone https://github.com/ShimaaELsaadi/Problem-Solving.git
   cd limak-vs-bob
   ```
2. Run the script:
   ```sh
   python limak_vs_bob.py
   ```
3. Enter values for `a` and `b` when prompted.

## Contributing
Feel free to open an issue or submit a pull request if you find any improvements!

## License
This project is open-source and available under the MIT License.

