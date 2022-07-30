from functools import lru_cache
import sys
sys.setrecursionlimit(10000)


lines = int(input())
juices = []
for _ in range(lines):
    a, b = input().split()
    juices.append((int(a), set(b)))

@lru_cache(None)
def dp(i: int , picked: tuple):
    if len(picked) == 4:
        return 0
    if i >= len(juices):
        return float("inf")
    s = set(picked)
    s.update(juices[i][1])
    check =dp(i+1,tuple(s) )

    pick = juices[i][0] + check
    not_pick = dp(i+1, picked)
    return min(pick, not_pick)


ans = dp(0, ('z',))
if ans != float("inf"):
    print(ans)
else:
    print(-1)
