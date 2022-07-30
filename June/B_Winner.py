n = int(input())

scores = {}
maxScore = (0,"")
for _ in range(n):
    name, s = list(map(str, input().split()))
    if name in scores:
        scores[name] += int(s)
    else:
        scores[name] = int(s)
    if scores[name] > maxScore[0]:
        maxScore = (scores[name], name)


# print(scores)
names = sorted(scores, key = scores.get)
print(maxScore[1])