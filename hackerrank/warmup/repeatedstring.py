#!/bin/python3

import os

# Complete the repeatedString function below.
def repeatedString(s, n):
    current_index = 0
    
    #Stores the number of a's seen until index i 
    lpa = []
    for digit in s:
        if(digit == 'a'):
            if(not lpa): lpa.append(1)
            else: lpa.append(lpa[current_index - 1] + 1)
        else:
            if(not lpa): lpa.append(0)
            else: lpa.append(lpa[current_index - 1])
        
        current_index += 1

    # Calculates the amount of the word s fits in n
    full_word = int(n / current_index)

    # Calculates the amount of letters that should sum to full word to equal n
    remainder = n % current_index
    
    if(remainder == 0): return full_word * lpa[-1]
    else: return full_word * lpa[-1] + lpa[remainder - 1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')
    fptr.close()
