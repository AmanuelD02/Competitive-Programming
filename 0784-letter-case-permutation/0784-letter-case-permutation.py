class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        answer = [list(s)]
        
        for i in range(n):
            if s[i].isdigit():
                continue
            for j in range(len(answer)):
                perm = answer[j]
                copy = perm[:]
                if s[i].isupper():
                    copy[i] = copy[i].lower()
                else:
                    copy[i] = copy[i].capitalize()
                    
                answer.append(copy)
        
        
        return ["".join(ans) for ans in answer]