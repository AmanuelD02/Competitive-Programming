# https://leetcode.com/problems/sorting-the-sentence/
class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split(" ")
        c = 0
        while c<len(lst):
            print(lst)
            print(str(c+1), lst[c][-1])
            if lst[c][-1] == str(c+1):
                lst[c] = lst[c][:-1]
                c+=1
            else:
                index = int(lst[c][-1])
                lst[index-1] , lst[c] = lst[c], lst[index-1]
                
                
        print(lst)
        return " ".join(lst)