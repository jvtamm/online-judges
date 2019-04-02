#!/bin/python3

import os

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    altitude = 0

    for step in s:
        if(altitude == -1 and step == 'U'): valleys += 1
        altitude = altitude + 1 if step == 'U' else altitude - 1

    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')
    fptr.close()
