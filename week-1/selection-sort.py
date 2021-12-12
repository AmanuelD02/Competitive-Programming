
class Solution: 
    def select(self, arr, i):
        # code here
        Min = i
        
        for j in range(i, len(arr)):
     
            if arr[j] < arr[Min]:
            
                Min = j
        return Min
            
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            min = self.select(arr,i)
    
            arr[i], arr[min] = arr[min], arr[i]
        return arr

