from os import stat


n = int(input())
stocks = list(map(int, input().split()))
total = 0
dp = {}
def segni(i, state, back, indx):
    if i >= len(stocks):
        return 0
    if (i, state) in dp:
        return dp[(i, state)]
    indx = indx if stocks[i] > stocks[indx] else i
    if state:
        sell =segni(i+1, not state, back, indx) + stocks[i]
    if not state:
        buy = segni(i+1, not state, back, indx) - stocks[i]
    b = 0
    if back and not state:
        b = segni(indx, False, 0, 0) + stocks[i] - stocks[indx]

    nothing = segni(i+1, state, back, indx)

    if state:
        dp[(i, state)] = max(nothing, sell, b)
    else:
        dp[(i, state)] = max(nothing, buy, b)
    
    return dp[(i, state)]

print(segni(0, False,1,0))
