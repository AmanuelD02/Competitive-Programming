test_case = int(input())

for _ in range(test_case):
    ans = set()
    s = input()
    
    left = right = 0
    while right < len(s):
        if s[left] == s[right]:
            right +=1
        else:
            if (right - left) %2 ==1:
                ans.add(s[left])
                left = right
    
    if left != right and (right - left) %2 ==1:
        ans.add(s[left])
        left = right

    ans = list(ans)
    print(''.join(ans))