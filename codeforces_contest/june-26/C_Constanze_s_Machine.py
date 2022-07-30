message = input()

def solve(msg):
    if 'w' in msg or 'm' in msg:
        return 0
    
    total = 0
    for i in range(len(msg)-1):
        aa = msg[i: i+2]
        if aa == 'uu' or aa =='nn':
            total += 1
    # print(total)
    return 2**total


MOD = 10**9 + 7
print(solve(message) %MOD)