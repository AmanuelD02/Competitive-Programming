test_cases = int(input())
for _ in range(test_cases):
    r, c = list(map(int,input().split()))
    if r==1 and c ==1:
        print(0)
        continue
    elif (r==1 and c> 2) or (c==1 and r>2):
        print(-1)
        continue
    else:
        Max = max(r,c)
        Min = min(r,c)
        if (Max -Min) %2==1:
            print(2*Max- 3)
        else:
            print(2*Max-2)
