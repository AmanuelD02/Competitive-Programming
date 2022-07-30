import sys
input = sys.stdin.readline
 
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
 
def count_health(k, lst):
    total = k
    for i in range(len(lst) -1):
        total += min(k, lst[i+1] - lst[i])
    return total
 
def monocarp(health, attacks):
    left , right = 1, health
    while left <= right:
        mid = (left + right) //2
        val  = count_health(mid, attacks)
        if val==health:
            return mid
        if val > health:
            right = mid -1
        else:
            left = mid +1
    return left
 
 

tests = inp()
for test in range(tests):
    _, health = inlt()
    attacks = inlt()
    print(monocarp(health, attacks))
 