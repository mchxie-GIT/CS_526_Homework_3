"""Problem 2: find unique substrings using recursion."""

import sys


def add_substrings(text, start, end, substrings):
    if end > len(text):
        return
    substrings.add(text[start:end])
    add_substrings(text, start, end + 1, substrings)


def find_substrings(text, start, substrings):
    if start == len(text):
        return
    # Find substrings starting here, then move to the next position.
    add_substrings(text, start, start + 1, substrings)
    find_substrings(text, start + 1, substrings)


def main():
    text = sys.stdin.readline().rstrip("\r\n")
    substrings = set()
    find_substrings(text, 0, substrings)
    for substring in sorted(substrings):
        print(substring)
    print(len(substrings))


if __name__ == "__main__":
    main()
