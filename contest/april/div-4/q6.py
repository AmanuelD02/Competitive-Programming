from collections import deque
from pprint import pprint


test_cases = int(input())

for _ in range(test_cases):
    row,col = list(map(int,input().split()))
    grid = []
    for r in range(row):
        one  = input()
        grid.append([x for x in one])
    # print(grid)

    for c in range(col):
        queue = deque()
        for r in range(row-1,-1,-1):
            if grid[r][c] == 'o':
                queue = deque()
            elif grid[r][c] == '.':
                queue.append(r)
            else:
                if queue:
                    rr = queue.popleft()
                    grid[rr][c] = '*'
                    grid[r][c] = '.'
                    queue.append(r)
    for i in grid:
        for j in i:
            print(j,end="")
        print("\n")