
tests = int(input())

def calculate(n, m, a):
    total = 0
    if n <= 2:
        return total
    a.sort()
    total = 2
    num_m = 0
    while n > total and a:
        num_m+= 1
        total -= 1
        total += a.pop()
    if n <= total:
        return num_m
    return -1

for _ in range(tests):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))

    print(calculate(n, m, a))

