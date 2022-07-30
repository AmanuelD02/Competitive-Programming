import math
tests = int(input())

for _ in range(tests):
    word = input()
    diff = set()
    days = 0
    for i in word:
        # print(diff)
        diff.add(i)
        if len(diff) == 4:
            days += 1
            diff.clear()
            diff.add(i)
    # printx`(diff)
    if diff:
        days += 1
    print(days)
