tests = int(input())
M = 7 + (10**9)
# print(M)
for _ in range(tests):
    n, k = list(map(int, input().split()))
    ans = 0
    c = 0
    while k:
        a = k & 1
        if a:
            # print(a)
            ans += (n**c)
        k >>= 1
        c += 1
    print(ans % (10**9 + 7))
