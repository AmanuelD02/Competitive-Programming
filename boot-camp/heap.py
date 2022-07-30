class Solution:
    def __init__(self,arr) -> None:
        self.arr = arr
        self.size = len(arr)
        self.buildHeap()

    #Heapify function to maintain heap property.
    def heapify(self,index):
        # code here
        pass
    #Function to build a Heap from array.
    def buildHeap(self):
        # code here
        pass
    


    def upHeap(self,index):
        while self.parent(index)!= None:
            parent = self.parent(index)
            if self.arr[parent] < self.arr[index]:
                self.arr[parent] , self.arr[index] = self.arr[index], self.arr[parent]
                index = parent
            else:
                break
            
    def downHeap(self,index):
        pass


    def insert(self,element):
        self.arr.append(element)


    def remove(self,index):
        self.arr[index], self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1] , self.arr[index]
        self.arr.pop()
        self.heapify()

    def update(self,index, element):
        self.arr[index] = element
        self.heapify()

    def getMax(self):
        return self.arr[0]

    def leftChild(self, index):
        left = (index *2) +1
        if left > len(self.arr)-1:
            return None
        return left

    def isLeaf(self,index):
        return (index *2) >= self.size

    def rightChild(self,index):
        right = (index*2) +2
        if right > len(self.arr)-1:
            return None
        return right
        
    def parent(self,index):
        if index ==0:
            return None
        return (index -1) //2
