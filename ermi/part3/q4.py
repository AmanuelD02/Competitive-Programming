
year,mon,day = eval(input())

days = {1:31, 2:28, 3:31, 4:30,5:31, 6:30, 7:31, 8:31, 9:30, 10:31,11:30,12:31}
isleap = lambda Y:  (Y %4 ==0 or Y%400 == 0 ) and Y%100 !=0
total = 0
for i in range(1, mon ):
    if i ==2:
        if isleap(year):
            total += 29
        else:
            total += 28
    else:
        total += days[i]

print(total + day-1)