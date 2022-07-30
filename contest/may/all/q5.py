n = int(input())
stocks = list(map(int, input().split()))
total = 0
dp = {}
def segni(i, state, stocks):
    if i >= len(stocks):
        return 0
    if (i, state) in dp:
        return dp[(i, state)]
    

    if state:
        sell =segni(i+1, not state, stocks) + stocks[i]
    if not state:
        buy = segni(i+1, not state, stocks) - stocks[i]
    
    nothing = segni(i+1, state, stocks)

    if state:
        dp[(i, state)] = max(nothing, sell)
    else:
        dp[(i, state)] = max(nothing, buy)
    
    return dp[(i, state)]


def reversed(stocks):
    N, profit = len(stocks), 0
    min_p = N - 1
    sell_P = 0
    buy_p = N -1
    for i in range(N-1, -1,-1):
        j = stocks[i]
        if j - stocks[min_p] > profit:
            profit =  j - stocks[min_p]
            sell_P = i
            buy_p = min_p
        min_p = min(min_p, j)

    return (profit, sell_P, buy_p)



p1, start, end  = reversed(stocks)
# print(start, end, sep="--")
total += p1
# print("1", total)
total += segni(0, False, stocks[: end + 1])

# print("2", total)
dp = {}
total += segni(0, False, stocks[start:])

print(total)
