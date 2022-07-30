dst = list(map(int, input().split()))

total = 0
dst.sort()
mid = dst[len(dst)//2]
for num in dst:
    total += abs(num-mid)

print(total)