# https://leetcode.com/problems/design-circular-deque/
from typing import *

class MyCircularDeque:

    def __init__(self, k: int):
        self.queue  = [None] * k
        self.front = 0
        self.back = 0
        

    def insertFront(self, value: int) -> bool:
        if (self.front-1) % self.k == self.back:
           return False

        self.front = (self.front-1) % self.k
        self.queue[self.front] = value


        return True

    def insertLast(self, value: int) -> bool:
        if self.front== (self.back +1)%self.k:
            return False
        
        self.back = (self.back +1) % self.k
        self.queue[self.back] = value
        

    def deleteFront(self) -> bool:
        if self.back == self.front:
            return False
        self.front = (self.front + 1) % self.k

        return True
        


        

    def deleteLast(self) -> bool:
        if self.back == self.front:
            return False
        self.front = (self.front + 1) % self.k

        return True

        

    def getFront(self) -> int:
        if self.front == self.back:
            return -1
        
        return self.queue[self.front]
        

    def getRear(self) -> int:
        if self.front == self.back:
            return -1
        
        return self.queue[self.back]
        

    def isEmpty(self) -> bool:
        return self.front == self.back
            
        
        

    def isFull(self) -> bool:
        return (self.front +1) % self.k ==self.back
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()