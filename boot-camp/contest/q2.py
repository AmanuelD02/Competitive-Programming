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
sushi = inlt()

Max= 0
last = sushi[0]
lastCount = current = 0
for i in sushi:
    if i==last:
        current +=1
    else:
        val =min(current, lastCount)*2
        Max = max(val, Max)
        last =i
        lastCount = current
        current =1
val = min(current, lastCount)*2

print(max(val, Max))