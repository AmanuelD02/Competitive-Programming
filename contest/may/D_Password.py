word = input()

def solve(word):
    ERROR = "Just a legend"
    freq = set(word)
    if len(freq) == 1:
        return ERROR
    
    start = word.find(word[-1])
    if start == len(word) -1:
        return ERROR
    
    search = word[:start + 1]
    if search in word[start + 1: - start]:
        return search
    return ERROR


print(solve(word))


