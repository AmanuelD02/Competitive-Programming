class Solution:
    def canMerge(self, interval1, interval2):
        return interval1[1] >= interval2[0]
    
    
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        len_first, len_second = len(firstList), len(secondList)
        
        p1 = p2 = 0
        result = []
        
        while p1 < len_first and p2 < len_second:
            interval_1, interval_2 = sorted([firstList[p1], secondList[p2]])
            
            if self.canMerge(interval_1, interval_2):
                merged = [max(firstList[p1][0], secondList[p2][0]), min(firstList[p1][1], secondList[p2][1])]
                result.append(merged)
            
            if firstList[p1][1] > secondList[p2][1]:
                p2 += 1
            else:
                p1 += 1
            
        
        return result
                                                                        
        