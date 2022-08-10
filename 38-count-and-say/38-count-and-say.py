class Solution:
    @lru_cache()
    def countAndSay(self, n: int, s="1") -> str:
        if n == 1:
            return s
        return self.countAndSay(n-1, self.counter(s))
                
                

            
    def counter(self, s):
        res = []
        cur = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] != cur:
                res.extend([str(count), cur])
                count = 0
                cur = s[i]
            count += 1

        res.extend([str(count), cur])
        return "".join(res)
            
            