class RandomizedCollection:

    def __init__(self):
        self.lookup = defaultdict(set)
        self.arr = []
        

    def insert(self, val: int) -> bool:
        self.lookup[val].add(len(self.arr))
        self.arr.append(val)
        
        return len(self.lookup[val]) == 1
        
    
    def remove(self, val: int) -> bool:
        if val not in self.lookup:
            return False
        last_element = self.arr[-1]
        if val != last_element:
            val_idx = self.lookup[val].pop()
            
            self.lookup[last_element].remove(len(self.arr) -1)
            self.lookup[last_element].add(val_idx)
            
            self.arr[val_idx] = last_element
        else:
            self.lookup[last_element].remove(len(self.arr) -1)
        
            
        self.arr.pop()        
        if not self.lookup[val]:
            del self.lookup[val]
        
        return True

    def getRandom(self) -> int:
        return choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()