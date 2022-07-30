tests = int(input())
for i in range(tests):
    n = int(input())
    k = 0
    n >>=1
    while n:
        k+=1
        n>>=1
    


    print((2**k)-1)
