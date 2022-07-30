


n = int(input())
Bx, By = list(map(int, input().split()))
Ax, Ay = list(map(int, input().split()))
Cx, Cy = list(map(int, input().split()))


def s():

    if Ax > Bx and Ay > By:
        if Cx > Bx and Cy > By:
            return "YES"

    if Ax > Bx and Ay < By:
        if Cx > Bx and Cy < By:
            return "YES"

    if Ax < Bx and Ay < By:
         if Cx < Bx and Cy < By:
            return "YES"


    if Ax < Bx and Ay > By:
        if Cx < Bx and Cy > By:
            return "YES"
    return "NO"



print(s())

































# in_bound = lambda  x,y : 1<= x <= n and 1<= y <= n

# directions = [[-1,0],[-1,-1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,1]]


# visited = set()
# def is_valid(x, y):
#     return in_bound(x,y) and (x,y) not in visited  and x != Bx and y != By and (Bx +  By) != x + y and (By - Bx )!= y - x 


# visited.add((Ax, Ay))
# def dfs(x,y):
#     # print(x, y)
#     if x == Cx and y == Cy:
#         return True

#     ans = False
#     for i in [-1, 0, 1]:
#         for j in [-1, 0, 1]:

#             if is_valid(i + x, j + y):
                
#                 visited.add((i + x, j + y))
#                 ans = ans or dfs(i + x, j + y)
#             else:
#                 if (x + i, y+ j)== (Cx,Cy):

#                     print("fd")
#     return ans

# a = 'YES' if dfs(Ax, Ay) else "NO"



# print(a)

