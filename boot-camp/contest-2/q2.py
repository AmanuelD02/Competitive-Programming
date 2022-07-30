import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

n , m = inlt()
questions = inlt()
questions.sort()
for i in range(n):
    st = inp()
    # index = min(len(questions)-1, st)

    left , right = 0 , len(questions) -1
    
    while left <= right:
        mid = (left + right) //2
        val = questions[mid]
        if val >= st:
            right = mid -1
        else:
            left = mid +1
    mid = (len(questions)//2) 
    if  0< left <=mid:
        print("YES")
    else:
        print("NO")