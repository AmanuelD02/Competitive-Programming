from collections import deque
from typing import *
from heapq import heapify, heappop, heappush
def leastInterval(tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    heap = list(map(lambda x: -x, count.values()))

    heapify(heap)
    tasks = 0
    while heap:
        maxx = heappop(heap) + 1
        tasks += 1
        arr = []
        for i in range(n):
            if maxx == 0 and not heap:
                break
            elif heap:
                poped = heappop(heap) +1
                if poped != 0:
                    arr.append(poped)
            tasks += 1
        if maxx != 0: heappush(heap , maxx)
        for i in arr:
            heappush(heap, i)
    return tasks





    # di = list(c.items())

    # total = 0


    # hq.heapify(di)
    # print(di)
    # queue = deque()

    # # Remove K elements from 
    # for i in range(n+1):
    #     queue.append(di.pop())
    
    # print(queue)
    # print(di)

    # while(queue):
    #     total +=1
    #     current  = queue.popleft()
    #     current = (current[0], current[1]-1)
    #     di.append(current)

    # print(di)








# print(Interval(["A","A","A","B","B","B","C","C","C","C"], 2))
print(leastInterval(["A","A","A","B","B","B","C"], 2))