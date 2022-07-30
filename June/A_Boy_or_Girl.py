
def solve(username):
    username = set(username)
    if len(username) %2 == 0:
        return "CHAT WITH HER!"
    return "IGNORE HIM!"




username = input()

print(solve(username))