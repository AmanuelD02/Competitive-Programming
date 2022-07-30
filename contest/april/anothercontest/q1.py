from collections import defaultdict



test_cases = int(input())
for _ in range(test_cases):
    N = int(input())
    ary = list(map(int, input().split()))

    freq = defaultdict(int)
    FLAG = True
    for i in ary:
        freq[i] += 1
        if freq[i]>=3:
            print(i)
            FLAG = False
            break
    if FLAG:
        print(-1)
