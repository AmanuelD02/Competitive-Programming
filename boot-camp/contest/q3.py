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


n = inp()

shops = inlt()
coins = []
ans = []
d = inp()
for i in range(d):
    coins.append(inlt()[0])

shops.sort()
FLAG = True
for c in coins:
    left , right = 0 , n-1
    f =0
    while left <= right:
        mid = (left + right)//2
        val  = shops[mid]
        if val== c:
           left = mid +1
           f= left+1
            
        elif val > c:
            right = mid -1
        else:
            left = mid +1
            f = left +1
    
    ans.append(f-1)
    
    # left = min(n-1, left)
    # val = shops[left]
    # if val <= c and left >=right:

    #     ans.append(left+1)
    # else:
    #     ans.append(0)
for a in ans:
    print(a)