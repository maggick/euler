#!/usr/bin/env python3

"""
Some positive integers n have the property that the sum [ n + reverse(n) ]
consists entirely of odd (decimal) digits.
For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers
reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not
allowed in either n or reverse(n).
There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
"""


def isReversible(n):
    if n % 10 == 0:
        return False
    m = n + int(str(n)[::-1])
    for c in str(m):
        if int(c) % 2 == 0:
            return False
    return True


def main():
    m = 10**9
    i = 1
    res = 0
    while i < m+1:
        if isReversible(i):
            res += 1
        i += 1
    print (res)


if __name__ == "__main__":
    main()
