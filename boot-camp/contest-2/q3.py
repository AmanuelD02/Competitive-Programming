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


def merger(a, b):
    if (a[1] +1) < b[0]:
        return False
    ans = (a[0], max(b[1], a[1]))
    return ans

n, tests = inlt()
days = []
for _ in range(tests):
    s1, s2 = inlt()
    days.append((s1,s2))
    

days.sort()
def solve():
    ans = days[0]
    if ans[0] != 0: return "YES"
    for i in range(1, len(days)):
        ast = days[i]

        m = merger(ans,ast)
        # print(m)
        if not m: return "YES"
        ans = m
    # print(ans)
    if ans[1] +1 != n: return "YES"
    return "NO"

print(solve())

