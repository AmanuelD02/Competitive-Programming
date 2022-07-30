class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        stop, counter = 2, 0
        for i in range(1, n+1):
            if i ==stop:
                counter = 0
                stop *=2
            res.append(1+ res[counter])
            counter +=1
        
        return res