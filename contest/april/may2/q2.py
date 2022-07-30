
from collections import Counter
tests = int(input())
def isPalindrome(word):
    l, r= 0 , len(word)-1
    while l<=r:
        if word[l] != word[r]:
            return False

        l+=1
        r-=1
    return True


def solve(word):
    # word= list(word)
    for i in range(len(word)):
        w = word[:i] + 'a' + word[i:]
        pal = isPalindrome(w)
        if not pal:
            return w
    w = word + 'a'
    pal = isPalindrome(w)
    if not pal:
        return w

    return False

def solve2(word):
    w1 = 'a' + word
    w2 = word + 'a'
    if not isPalindrome(w1):
        return w1
    if not isPalindrome(w2):
        return w2
    return False

for _ in range(tests):
    word = input()
    freq  = Counter(word)
    if freq['a'] == len(word):
        print("NO")
    elif isPalindrome(word):
        print("YES")
        print('a' + word)
    else:
        pal = solve2(word)
        if not pal:
            print("NO")
        else:
            print("YES")
            print(pal)

    

    # pal = solve(word)
    # if not pal:
    #     print("NO")
    # else:
    #     print("YES")
    #     print(pal)

