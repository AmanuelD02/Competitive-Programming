class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            i = 0
            temp = []
            while i < len(s):
                temp.append(str(sum([int(x) for x in s[i:i+k]])))
                i+= k
            
            s= "".join(temp)
        return s
        