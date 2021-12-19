# https://leetcode.com/problems/number-of-recent-calls/


from typing import *
class RecentCounter:

    def __init__(self):
        self.queue = Deque()        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while(self.queue and t- self.queue[0] > 3000):
            self.queue.popleft()
        
        
        return len(self.queue)
            
        
        
        

            
            
            
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)s