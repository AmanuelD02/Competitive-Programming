tank = 0
road, fullT = list(map(int,input().split()))
if (road == fullT +1):
    print(fullT)
elif road == fullT:
    print(fullT -1)
elif road < fullT:
    print(road -1)
else:
    dist = road -1 -fullT
    c = 1
    tank += fullT
    for i in range(dist):
        c+=1
        tank+= c

    print(tank)