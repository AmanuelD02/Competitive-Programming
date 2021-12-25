

def repeatedString(s, n):
    # Write your code here
    count = 0
    for letter in s:
        if letter == 'a':
            count +=1
    ans = 0
    
    ans = (n//len(s)) * count
    # print(ans)
    
    temp = n % len(s)
    for i in range(temp):
        if s[i] == 'a':
            ans +=1
    print(ans)
    return ans



repeatedString("aba",10)