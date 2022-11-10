class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:       
        N = len(points)
        
        freq_line = defaultdict(set)
        
        for i in range(0, N):
            for j in range(i+1, N):
                line_formed = self.calculate_slope(points[i], points[j])
                
                freq_line[line_formed].add(tuple(points[i]))
                freq_line[line_formed].add(tuple(points[j]))
        
        max_points = 1
        for key, val in freq_line.items():
            max_points = max(max_points, len(val))
        
        return max_points
        
        
        # take two points
      # returns slope and y intercept      
    def calculate_slope(self, point1, point2):
        x = point2[0] - point1[0]
        if x == 0:
            return (inf, point1[0])
        slope = (point2[1] - point1[1] )/ (x)

        y_intercept = point1[1] - (point1[0] * slope)

        return (slope, y_intercept)