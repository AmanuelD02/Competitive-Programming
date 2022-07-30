tests = int(input())
def solve(num):
    if(int(num[-1])%2 == 0):
        return 0
    if(int(num[0])%2 == 0):
        return 1
    evens = {"2", "4", "6", "8"}
    for i in num:
        if i in evens:
            return 2
    return -1


for _ in range(tests):
    num = input()
    count = 0
    print(solve(num))
