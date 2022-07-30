from enum import Flag
import sys
input = sys.stdin.readline
from collections import Counter
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

_= inlt()
target =_[1]
lst = inlt()
def finder(lst, target):
    for i in range(len(lst)):
        innerTarget = target - lst[i]
        visited = {}
        for j in range(i+1, len(lst)):
            t = innerTarget - lst[j]
            if t in visited:
                return (i+1,j+1,visited[t]+1)
            visited[lst[j]] = j
    

ans = finder(lst,target)
if ans:
    print(ans[0], ans[1], ans[2] )
else:
    print("IMPOSSIBLE")