#!/bin/python3

import os

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n, c):
    jumps = 0
    index = 0
    
    while(index < n - 1):
        if (index + 2 < n and c[index + 2] == 0):
            index = index + 2
            jumps += 1
        elif(index + 1 < n and c[index + 1] == 0):
            index = index + 1
            jumps += 1

    return jumps

# A more general function that computes number of jumps accordingly to the size of max jump
def jumpingOnCloudsRange(n, c, max_jump):
    jumps = 0
    index = 0

    while(index < n - 1):
        for jump in range(max_jump, 0, -1):
            if(index + jump < n and c[index + jump] == 0):
                index += jump
                jumps += 1
    
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnCloudsRange(n, c, 2)

    fptr.write(str(result) + '\n')
    fptr.close()