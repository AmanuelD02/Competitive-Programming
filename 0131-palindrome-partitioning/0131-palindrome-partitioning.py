class Solution:
    def partition(self, s: str) -> List[List[str]]:
        s_size = len(s)
        def dp(start, end):
            if end >= s_size:
                return [[]]
            select = [[]]
            if s[start: end + 1] == s[start: end + 1][::-1]:
                select = dp(end + 1, end + 1)
                for word in select:
                    # if len(word) == 0: continue
                    word.append(s[start: end + 1])
            not_select = dp(start, end + 1)
            
            
            return select[:] + not_select[:]
            
        ans = dp(0, 0)
        new_ans = []
        for lst in ans:
            counter = 0
            for a in lst:
                counter += len(a)
            if counter == s_size:
                new_ans.append(reversed(lst))
        return new_ans