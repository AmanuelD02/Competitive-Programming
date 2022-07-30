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



tests = inp()
for _ in range(tests):
    target = inp()

    group1 = 31
    group2 = 32

    k2 = k1 = 0
    while group1 !=target:
        if group1 > target:
            group1 -=1
        else:
            group1 +=4
        k1 +=1
    
    while group2 != target:
        if group2 > target:
            group2 -=1
        else:
            group2 +=4
        k2+=1
    if k1 > k2:
        ans = 32
    else:
        ans = 31
    print(ans)

