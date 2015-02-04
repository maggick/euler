#!/usr/bin/env python3

"""
Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.
However, confirming that 632382518061 > 519432525806 would be much more
difficult, as both numbers contain over three million digits.
Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
containing one thousand lines with a base/exponent pair on each line,
determine which line number has the greatest numerical value.
"""


def main():
    f = open('p099_base_exp.txt', 'r')

    res = 0
    i=0
    j=0

    for l in f.readlines():
        print (i)
        i+=1
        r = (l.strip().split(','))
        tmp = int(r[0])**int(r[1])
        if tmp > res:
            j=i
            res = tmp
    print (j)

if __name__ == '__main__':
    main()
