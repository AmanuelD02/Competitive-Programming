def is_palindrome(lst):
    left , right = 0 , len(lst) -1
    if left == right: return False

    while left < right:
        if lst[left] != lst[right]:
            return False
        left +=1
        right -=1

    return True


tests = int(input())

for i in range(tests):
    bracket = input()
    stack = []
    a = b= 0
    for i in bracket:
        if i == ')' and stack and stack[-1] == '(':
            stack.pop() 
            a +=1
        
