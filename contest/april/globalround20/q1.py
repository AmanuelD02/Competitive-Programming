tests = int(input())
from heapq import heapify, heappop, heappush

for _ in range(tests):
    N = int(input())
    lst = list(filter( lambda x : x>=2  ,map(int, input().split())) )

    heapify(lst)
    turn = True
    while lst:
        big = heappop(lst)
        big -= 1
        if big >=2:
            heappush(lst, big)
        turn = not turn
    

    res = "errorgorn" if not turn else "maomao90"
    print(res)
    
