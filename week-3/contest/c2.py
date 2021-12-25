def equalStacks(h1, h2, h3):
    # Write your code here
    total1 = sum(h1)
    total2 = sum(h2)
    total3 = sum(h3)

    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]

    while( not total1 == total2 == total3):
        
        if h1 == [] or h2 ==[] or h3 ==[]:
            print(h1, h2, h3)
            return 0

        maxx = max(total1, total2, total3)
        # print(total1, total2, total3)
        if maxx == total1:
            total1 -= h1.pop()
        elif maxx == total2:
            total2 -= h2.pop()
        else:
            print(h3[-1])
            total3 -= h3.pop()
            
    print("while")
    print(total1, total2, total3)
    print(h1, h2, h3)

    return total1




a =equalStacks([19, 74,  60 ,60 ,16 ,45 ,16 ,10 ,6, 46, 87, 34, 61, 15, 71, 66, 3 ,6 ,97 ,18 ,84,19], [19,19,18], [18,19])
print(a)