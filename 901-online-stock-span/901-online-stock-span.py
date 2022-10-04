class StockSpanner:

    def __init__(self):
        self.counter = 0
        self.stack = []

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        last = -1 if not self.stack else self.stack[-1][1]
        self.stack.append([price,self.counter])
        self.counter += 1
        # print(self.counter,last,self.stack)
        return self.counter - last - 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)