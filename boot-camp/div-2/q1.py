import math
tests = int(input())
for i in range(tests):
    a, b = list(map(int, input().split()))
    if a ==0 and b ==0:
        print(0)
        continue
    cc = (a*a) + (b*b)
    bb = math.sqrt(cc)
    if math.floor(bb) == bb:
        print(1)
        continue

    print(2)