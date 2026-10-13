import sys


def is_palindrome(text):
    # Ignore spaces, but keep upper and lower case different.
    text = text.replace(" ", "")
    return text == text[::-1]


def main():
    count = 0
    for line in sys.stdin:
        result = is_palindrome(line.rstrip("\r\n"))
        print(result)
        if result:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
