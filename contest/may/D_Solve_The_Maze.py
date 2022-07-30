from functools import lru_cache


visited =set()
tests = int(input())
directions = [(0,1), (1,0), (0,-1), (-1, 0) ]


def dfs(i, j, end):
    if (i,j) == end:
        return True
    visited.add((i,j))
    cal = False

    for x, y in directions:
        if in_bound(i + x, j + y) and (i + x, j + y) not in visited and grid[i + x][ j + y] !='#' and grid[i + x][ j + y] !='B':
            cal = cal or dfs(i + x, j + y, end)
    return cal
    
    



    

def change(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'B':
                # print(i,j)
                for x, y in directions:
                    # print(i + x, j+ y)
                    if in_bound(i + x, j+ y) and grid[i + x][j+ y] =='.':
                        # print("ga")
                        grid[i+x][j+y] = '#'
     

def travel(grid, end):
    f = True
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'G':
                
                f = f and dfs(i, j, end)
                if not f: return False
    return f

for _ in range(tests):
    n, m = list(map(int, input().split()))
    in_bound = lambda x, y: 0 <= x < n and 0 <= y < m
    visited.clear()
    grid = []
    for i in range(n):
        row = input()
        grid.append([x for x in row])
    change(grid)
    # print(grid)
    f = travel(grid, (n-1, m-1))
    if f: 
        print("Yes")
    else:
        print("No")


