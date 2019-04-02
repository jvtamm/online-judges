#!/bin/python3

import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    colors = set()

    for color in ar:
        if (color in colors):
            pairs += 1
            colors.remove(color)
        else:
            colors.add(color)
    return pairs


if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')
    fptr.close()