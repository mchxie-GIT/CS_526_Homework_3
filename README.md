# CS526 Homework 3

## Introduction

These programs check palindromes, recursively find unique substrings, recursively reverse three stack implementations, and check whether Ghostbusters' streams cross. They use only standard Python.

## Algorithm

- **Problem 1:** Remove spaces and compare the string with its reverse. Print each result and count the palindromes. Case is preserved.
- **Problem 2:** One recursive function extends a substring's ending position. Another moves its starting position. A set removes duplicates, and sorting gives alphabetical output.
- **Problem 3:** The array stack uses a Python list. The singly linked stack stores the top node and its next link. The doubly linked stack also maintains previous links. Reversal removes the top value, reverses the rest recursively, then inserts the removed value at the bottom recursively. The same function works with all three stacks and changes the original stack object.
- **Problem 4:** For each pair of streams, compare their direction vectors using integer multiplication. Nonparallel infinite lines cross. For parallel lines, check whether one starting point lies on the other line. If so, the lines coincide and count as crossing. Otherwise, they do not cross. All ghosts are eliminated only if every pair passes these checks.

## Interesting aspects

- The palindrome check ignores spaces but distinguishes `A` from `a`.
- Substrings contain consecutive characters; the empty substring is excluded.
- Stack reversal uses no loops and no second stack. Its running time is O(n²). Loops are used only to build and display the example stacks.
- Ghostbusters' pairs stay unchanged. Integer calculations handle vertical lines and avoid rounding errors. Checking all pairs takes O(n²) time.

## How to run

Run these commands from inside the `Homework3` folder:

```bash
python3 problem1.py < tests/problem1_basic.txt
python3 problem2.py < tests/problem2_basic.txt
python3 problem3.py
python3 problem4.py < tests/problem4_crossing.txt
python3 test_homework3.py
```

On Windows PowerShell, use `Get-Content` instead of `<`, for example:

```powershell
Get-Content tests/problem1_basic.txt | python problem1.py
Get-Content tests/problem2_basic.txt | python problem2.py
python problem3.py
Get-Content tests/problem4_crossing.txt | python problem4.py
python test_homework3.py
```

`example_executions.txt` contains the example commands and their actual outputs. Problem 3 pushes 1 through 10 automatically; its output shows the array, singly linked, and doubly linked stacks in that order.

## Submission

Add this entire `Homework3` folder to your existing Git repository, commit and push it, then submit the repository link on Brightspace.
