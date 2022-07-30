tests = int(input())


for _ in range(tests):
    n, target = list(map(int, input().split()))
    num = list(map(int, input().split()))
    Sum = sum(num)
    targetSum = Sum - target
    # for i in range(1, n):
    #     num[i] = num[i -1] + num[i]
    # num.append(0)
    ans = 0
    left = right = 0
    cur = 0
    if target == Sum:
        # print(0)
        continue
    while right < n:
        if cur == targetSum:
            ans = max(ans, right - left)
        if cur > targetSum:
            cur -= num[left]
            left += 1
        else:
            cur += num[right]
            right += 1
    print(ans)





