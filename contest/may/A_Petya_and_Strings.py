

word1 = input()
word2 = input()

word1 = word1.lower()
word2 = word2.lower()
if word1 == word2:
    print(0)
elif word1 > word2:
    print(1)
else:
    print(-1)
