tests = int(input())

def check(word, target):
    for i,j in enumerate(word):
        if j== target:
            if i%2 ==0 and (len(word) - i-1) %2 ==0:
                return "YES"
    return "NO"
for i in range(tests):
    word = input()
    target = input()
    print(check(word, target))
