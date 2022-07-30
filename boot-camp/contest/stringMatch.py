
from cProfile import run


def hash_string(s):
    p = 1
    result = 0
    m = 1000000007

    for i in range(len(s)-1, -1, -1):
        result = (result + (p * (ord(s[i]) - ord("a") + 1))) % m
        p *= 26
    
    return int(result)

word = input()
pattern = input()
k = len(pattern)

p = 26 ** (k - 1)
pattern_hash = hash_string(pattern)
running_hash = hash_string(word[:k-1])
count = left = 0
m = 1000000007
r = 0
for right in range(k-1, len(word)):
    running_hash = (running_hash * 26)  % m
    running_hash = (running_hash + ord(word[right]) - ord("a") + 1) % m
    running_hash = int(running_hash)

    if running_hash == pattern_hash:
        count += 1
    
    running_hash = running_hash - (p * (ord(word[left]) - ord("a") + 1)) % m
    left += 1

print(count)



