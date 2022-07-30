
from collections import defaultdict
import sys
sys.setrecursionlimit(3000)

tests = int(input())
___ = input()
for line in range(tests):
    check = list(map(int, input().split()))

    a, b  = check

    nums = list(input().split())
    # pre calculate
    preCalc = defaultdict(list)
    for i in range(len(nums)):
        preCalc[nums[i]].append(i)
    ans = []

    for __ in range(b):
        start, end = list( input().split())
        if start in preCalc and end in preCalc and preCalc[start][0] < preCalc[end][-1]:
          
            print("YES")
        else:
            print("NO")
    # print(*ans, sep="\n")
    if line < tests-1:
        __ = input()
