test_cases = int(input())
def isValid(red, blue):
    if red == 0 and blue == 0: return True

    if red ==0 or blue ==0: return False
    return True

for _ in range(test_cases):
    N = int(input())
    colors = input()
    red = blue = 0
    FLAG = True
    for i in colors:
        if i == 'W':
            if isValid(red, blue):
                blue = red = 0
            else:
                print("NO")
                FLAG = False
                break
        elif i == "B":
            blue += 1
        else:
            red += 1
    if FLAG:
        if isValid(red, blue):
            print("YES")
        else:
            print("NO")



        