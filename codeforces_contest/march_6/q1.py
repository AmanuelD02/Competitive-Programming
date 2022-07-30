from os import initgroups


tests = int(input())
for _ in tests:
    length = int(input())
    lst = list(map(int, input().split()))
    coins = 1
    last_traveled = None
    coin_spent =0
    right =0
    while right <len(lst):
        if lst[right]:
            right +=1
            if not last_traveled:
                last_traveled = right
            continue

        if coins:
            coins -=1
            temp = right
            while right < len(lst) and not lst[right]:
                right +=1
            coin_spent = right - temp
        else:
            break
    if coins:
        print("0")
    elif coins==0 and right!= length-1:
        print(last_traveled - length+1)
    else:
        print(coin_spent)
