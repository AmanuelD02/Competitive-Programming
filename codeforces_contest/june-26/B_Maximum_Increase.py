n = int(input())
nums =  list(map(int, input().split()))

cur = max_con = 1
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        cur += 1
    else:
        cur = 1

    max_con = max(cur, max_con)

print(max_con) 