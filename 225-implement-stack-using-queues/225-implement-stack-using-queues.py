class Queue:
    
    def __init__(self):
        self.items = []
        
    def enqueue(self, value):
        self.items.insert(0, value)
        
        ## self.items.append(value)
        
    def dequeue(self):
        if self.isEmpty():
            return " Empty Queue. "
        return self.items.pop()
        
        ## self.items[0]
    
    
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.main = Queue()
        self.temp = Queue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.temp.enqueue(x)
        while(not self.main.isEmpty()):
            self.temp.enqueue(self.main.dequeue())
        self.main = self.temp
        self.temp = Queue()
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.main.dequeue()

    def top(self) -> int:
        """
        Get the top element.
        """
        temp = self.main.dequeue()
        self.push(temp)
        return temp
        
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.main.isEmpty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()