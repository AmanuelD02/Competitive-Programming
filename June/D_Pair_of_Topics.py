import bisect
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


c = [ a[i] - b[i] for i in range(N) ]
c.sort()
ans = 0
# print(c)
for i in range(N):
    val = c[i]
    if val >0:
        ans += (N -i-1)
        # print(N -i, i, val)

    else:
        place = bisect.bisect_right(c, -val)
        # print(c[i], place)
        ans += (N- place )
print(ans)
