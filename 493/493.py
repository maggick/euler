#!/usr/bin/env python3

"""
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.
What is the expected number of distinct colors in 20 randomly picked balls?
Give your answer with nine digits after the decimal point (a.bcdefghij).
"""

import random


def main():
    i = 0
    # nombre d'essai
    j = 10000000
    color = 0
    while i < j:
        # prendre 20 boules au hasard
        balls = pikeBalls()
        # compte le nombre de couleurs différentes
        color += countBalls(balls)
        i += 1
    print ('{},{}'.format(j, color/j))


def pikeBalls():
    balls = []
    i = 0
    while i < 20:
        ball = random.randint(0, 69)
        while ball in balls:
            ball = random.randint(0, 69)
        balls.append(ball)
        i += 1
    return balls


def countBalls(balls):
    colors = [0, 0, 0, 0, 0, 0, 0]
    color = 0
    for ball in balls:
        tmp = int(ball/10)
        colors[tmp] += 1

    for elem in colors:
        if elem != 0:
            color += 1
    return color


if __name__ == '__main__':
    main()
