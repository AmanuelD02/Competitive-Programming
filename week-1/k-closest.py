class Solution:
    def kClosest(self, points, k):
        def compare(p1,p2):
            p11 = p1[0] **2 + p1[1]**2
            p22 = p2[0]**2 + p2[1]**2

            return p11< p22
        
        
        for i in range(k+1):
            Min = i
            for j in range(i,len(points)):

                if compare(points[j],points[Min]):
   
                    Min = j
            points[Min], points[i] = points[i], points[Min]


        return points[:k]
                
            
        
a = Solution()

a.kClosest([[3,3],[5,-1],[-2,4],[0,0]], 2)