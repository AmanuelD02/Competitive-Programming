n = int(input())


count = 0
while n:
    count += n & 1
    n >>= 1

print(count)