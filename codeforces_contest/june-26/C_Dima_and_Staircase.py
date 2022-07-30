n  = int(input())
heights = list(map(int, input().split()))
m = int(input())

for j in range(1, len(heights)):
    heights[j] = max(heights[j], heights[j-1])

res = []

for i in range(m):
    w, h = list(map(int, input().split()))
    ans = max(heights[0], heights[w-1])

    heights[0] = max(heights[0], ans + h)
    
    res.append(ans)


print(*res, sep="\n")