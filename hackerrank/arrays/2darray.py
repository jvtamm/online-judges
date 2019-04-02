#!/bin/python3

import os

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # Initialize max sum with minimum value possible
    max_sum = -63

    # Range could be 4 because matrix is 6x6 and hourglass is 3x3. Index 5 would need a 7x7
    for row in range(4):
        for col in range(4):
            current_sum = sum(arr[row][col: col + 3]) + arr[row + 1][col + 1] + sum(arr[row + 2][col: col + 3])
            print(current_sum)

            if(current_sum > max_sum): max_sum = current_sum

    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')
    fptr.close()