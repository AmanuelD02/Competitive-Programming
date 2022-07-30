from os import rename


test_case = int(input())

for _ in range(test_case):
    N = int(input())
    ary =  list(map(int,input().split()))
    b = ary[-1]
    a = sum(ary) - ary[-1] 