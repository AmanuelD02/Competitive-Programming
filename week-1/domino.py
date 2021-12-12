def solution():
    a= input()
    lst = a.split(" ")
    a, b = int(lst[0]), int(lst[1])
    if 1<= a <= 16 and  1<= b <= 16:
        result = (a*b) //2

        print(result)
    else:
        print()
solution()
