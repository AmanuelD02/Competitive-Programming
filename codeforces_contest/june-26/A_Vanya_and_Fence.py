n , m = list(map(int, input().split()))
heights =  list(map(int, input().split()))


total = 0
for h in heights:
    if h > m:
        total += 2
    else: 
        total += 1
print(total)