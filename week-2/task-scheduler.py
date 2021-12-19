from collections import deque
from typing import *
import heapq as hq
def leastInterval(tasks: List[str], n: int) -> int:
    c = Counter(tasks)
    di = list(c.items())

    total = 0


    hq.heapify(di)
    queue = deque()

    # Remove K elements from 
    for i in range(n):
        queue.append(di.pop())
    
    print(queue)
    print(di)

    while(queue):
        total +=1
        current  = queue.popleft()
        current[1] -=1



print(leastInterval(["A","A","A","B","B","B","C"], 2))