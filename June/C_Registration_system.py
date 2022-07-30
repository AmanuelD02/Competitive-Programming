
names = {}
tests = int(input())
for _ in range(tests):
    name  = input()
    if name not in names:
        names[name] = 0
        print("OK")
    else:
        names[name] += 1
        print(name + str(names[name]))
        