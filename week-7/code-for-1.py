from typing import *
globalRange = [3, 10]

def rescueSam (num: int, range : List[int])-> int: 
    if range[0] == range[1]:
        
        if globalRange[0] <= range[0] <= globalRange[1]:
            return num
        else:
            return 0

    if not ((range[0] >= globalRange[0] and range[0] <= globalRange[1]) or  (range[1] >= globalRange[0] and range[1] <= globalRange[1])):
        

        print("out of range", num, range)

        print("---")
        return 0
    if num==0 or num ==1:
        return num
    

    a,b ,c = num//2, num %2, num //2
    
    if a ==1 or a==0:
        a1, a2 = range[0], range[0]
    else:
        a1 , a2 = range[0], range[0] + a -1

    b1 , b2 = a2 +1 , a2 + 1
    if c ==1 or c ==0:
        c1, c2 = b2+1, b2+1
    else:

        c1, c2 = b2 +1, b2 +c
    print(num)
    print(a, a1, a2)
    print(b, b1, b2)
    print(c, c1, c2)
    print("----")
    return rescueSam(a,[a1,a2]) +   rescueSam(b,[b1,b2]) +   rescueSam(c, [c1,c2])



print("ans",rescueSam(10, [1,10]))