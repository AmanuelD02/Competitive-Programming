from collections import defaultdict
tests = int(input())
for _ in range(tests):
    n = int(input())
    lst = list(map(int, input().split()))
    ss = sum(lst)
    avg = ss / n
    wantedSum = avg * (n-2)
    nu = defaultdict(int)
    ans = 0
    # print(lst)
    for i in lst:
        ans += nu[ss -wantedSum - i]
        nu[i] += 1
    print(ans)
