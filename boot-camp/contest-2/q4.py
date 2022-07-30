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


n, tests = inlt()

days = [0] *n
for _ in range(tests):
    s1, s2 = inlt()
    for i in range(s1,s2+1):
        days[i] +=1

count = 0
for d in days:
    if d<=1:
        count+=1
print(count)