coins = int(input() )
lst = list(map(int, input().split()))
lst.sort(reverse= True)
total = sum(lst)
amount = 0
c = 0
# print(total, lst)
while total >= amount :
    total -= lst[c]
    amount += lst[c]
    c += 1
print(c)


