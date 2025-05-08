#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./factorial.py <positive_integer>")
        sys.exit(1)

    f = factorial(int(sys.argv[1]))
    print(f)
