class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        candies = [1] * N
        for i in range(N - 1):
            if ratings[i] == ratings[i+1]:
                ratings[i+1] = ratings[i]
            elif ratings[i] > ratings[i+1]:
                if candies[i] <= candies[i+1]:
                    candies[i] = candies[i+1] + 1
            else: 
                if candies[i] >= candies[i+1]:
                    candies[i+1] = candies[i] + 1
        

        for i in range(N-1,0,-1):
            if ratings[i] == ratings[i-1]:
                ratings[i-1] = ratings[i]
            elif ratings[i] > ratings[i-1]:
                if candies[i] <= candies[i-1]:
                    candies[i] = candies[i-1] + 1 
            else:
                if candies[i] >= candies[i-1]:
                    candies[i-1] = candies[i] + 1
                    
        return sum(candies)