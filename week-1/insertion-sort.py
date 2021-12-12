#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1,len(arr)):
        index = i
        current = arr[i]
        
        for j in range(i-1,-1,-1):
            
            if current < arr[j]:
                arr[index] = arr[j]
                index -=1
                for x in arr:
                    print(x,end=" ")
                print()
                 
            else:
                
                break
        arr[index] = current
    for x in arr:
        print(x,end=" ")
    print()
        
        
            
        
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
