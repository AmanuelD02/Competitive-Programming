class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0 , len(people) -1
        total = 0 
        while left < right:
            if people[left] + people[right] <= limit:
                left +=1
            
            right -=1
            total +=1
        if left ==right:
            total +=1
        
        return total