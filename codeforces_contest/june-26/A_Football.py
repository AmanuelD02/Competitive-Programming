players = input()

def solve(players):
    cur = players[0]
    total = 1
    for i in range(1, len(players)):
        if players[i] == cur:
            total += 1
        else:
            cur = players[i]
            total = 1
        if total == 7:
            return "YES"
    return "NO"


print(solve(players))