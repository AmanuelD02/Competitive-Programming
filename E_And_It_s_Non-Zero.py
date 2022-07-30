

table = [ [0 for x in range(20)] for y in range(2*10**5 + 1) ]

for i in range(1, 2*10**5 + 1):
    for k in range(20):
        if i & (1<<k) == 0:
            table[i][k] += table[i - 1][k] + 1
        else:
            table[i][k] = table[i - 1][k]



tests = int(input())

for _ in range(tests):
    s, e = map(int, input().split())
    res = float('inf')
    for i in range(20):
        res = min(res, table[e][i] - table[s-1][i])
    print(res)