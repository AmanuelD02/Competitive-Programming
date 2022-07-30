import math
tests = int(input())

def fun(x, a):
    return math.floor(x/a) + x%a


for _ in range(tests):
    li, ri, a = list(map(int, input().split()))

    a2 = fun(ri, a)
    z = ri - (ri%a)  -1
    if z >= li:
        print(max(fun(z,a), a2))
        continue  
    print(a2) 
    print(a2)     

