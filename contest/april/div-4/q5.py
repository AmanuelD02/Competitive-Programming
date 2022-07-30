from collections import defaultdict


test_cases = int(input())

def validstr(inp):
    a = set()
    for i in range(97, 108):
        temp = inp[0] + chr(i)
        temp2 = chr(i) + inp[1]
        if temp != inp: a.add(temp)
        if temp2 != inp: a.add(temp2)
    return a
            

for _ in range(test_cases):
    strings = int(input())
    freq = defaultdict(int)
    
    total = 0
    for i in range(strings):
        freq[input()] += 1
    visited = set() 
    for a in list(freq):
        coms = validstr(a)
        for i in coms:
            if i not in visited:
                total += (freq[a] * freq[i])
        visited.add(a)
    print(total)
    

    