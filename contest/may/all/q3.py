from collections import defaultdict
n, m = list(map(int, input().split()))

grid =  defaultdict(lambda: defaultdict(int))


def calculator(x1, y1, x2, y2, grid):
    total = 0
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            total += grid[x][y]
    
    return total



for _ in range(n):
    x, y = list(map(int, input().split()))
    grid[x][y]  += 1



for _ in range(m):
    x1, y1, x2, y2 = list(map(int, input().split()))
 
    print(calculator(x1, y1, x2, y2, grid))