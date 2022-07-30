columns = int(input())

def hiddenStudents(column):
    height = column[-1]
    total = 0

    for i in range(len(column)-2, -1,-1):
        h = column[i]
        if h < height:
            total += 1
        height = max(height, h)

    return total 

for _ in range(columns):
    __ = input()
    column = list(map(int, input().split()))

    print(hiddenStudents(column))

    
