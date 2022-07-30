days = {1:31, 2:28, 3:31, 4:30,5:31, 6:30, 7:31, 8:31, 9:30, 10:31,11:30,12:31}
year, month =eval(input())

if month !=2:
    print(days[month])
else:
    if (year %4 ==0 or year%400 == 0 ) and year%100 !=0:
        print(29)
    else:
        print(28)

