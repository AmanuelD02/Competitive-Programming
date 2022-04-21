class MyHashSet:

    def __init__(self):
        self.hash = [0] * ((10**6) +1)        

    def add(self, key: int) -> None:
        self.hash[key] = 1

    def remove(self, key: int) -> None:
        self.hash[key] = 0

    def contains(self, key: int) -> bool:
        return bool( self.hash[key])

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)