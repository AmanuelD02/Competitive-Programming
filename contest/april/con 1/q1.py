test_case = int(input())

for _ in range(test_case):
    SB = SR =  0
    N = int(input())
    RED, BLUE = input(), input()

    for i in range(N):
        if RED[i] > BLUE[i]:
            SR += 1
        if RED[i] < BLUE[i]:
            SB += 1
    
    if SB == SR:
        print("EQUAL")
    elif SB > SR:
        print("BLUE")
    else:
        print("RED")
        