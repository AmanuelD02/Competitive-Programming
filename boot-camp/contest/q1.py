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




a = inlt()


remaining = 240 - a[1]
total = 0
counter =1
for i in range(a[0]):
    if remaining - counter*5>=0:
        total +=1
        remaining -= counter*5
        counter+=1
    else:
        break
print(total)