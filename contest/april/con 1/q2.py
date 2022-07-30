numbers = int(input())
score = 0
neg = 0
zero = 0
nums = input()
nums = list(map(int, nums.split()))

for n in nums:
    if n < 0:
        score += abs(n + 1)
        neg += 1
    else:
        if n == 0:
            zero += 1
        score += abs(n-1)


if neg % 2 ==0:
    print(score)
elif zero > 0:
    print(score)
else:
    print(score + 2)
    
