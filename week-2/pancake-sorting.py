class Solution:
    def pancakeSort(self,arr):
        flips = []
        for i in range(len(arr),0,-1):
            # search for the max num
            index = arr.index(i)
            
            flips.append(index+1)
            # bring the top element to the front
            arr[0:index+1] = arr[0:index+1][::-1]
            # take the top element to its correct place
            arr[0:i] = arr[0:i][::-1]
            flips.append(i)
            
        print(arr)
        return flips
            