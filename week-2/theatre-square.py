import math
def solution():
    inp = input().split(" ")
    n, m , a = map(lambda x: int(x), inp)

    total = math.ceil(n/a) * math.ceil(m/a)
    print(total)
    return total 

solution()
