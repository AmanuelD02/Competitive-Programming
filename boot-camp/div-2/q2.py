tests = int(input())
for i in range(tests):
    n, B, x, y = list(map(int, input().split()))
    ans = 0
    ar = 0
    for i in range(n):
        if ar + x <= B:
            ar +=x
        
        else:
            ar -=y
        ans += ar
    
    print(ans)
