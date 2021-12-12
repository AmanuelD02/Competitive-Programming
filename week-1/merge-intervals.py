# https://leetcode.com/problems/merge-intervals/
class SelectionSort: 
    def select(self, arr, i):
        # code here
        Min = i
        
        for j in range(i, len(arr)):
     
            if arr[j][0] < arr[Min][0]:
            
                Min = j
            elif arr[j][0] == arr[Min][0]:
                if arr[j][1] < arr[Min][1]:
                    Min = j
        return Min
            
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            min = self.select(arr,i)
    
            arr[i], arr[min] = arr[min], arr[i]

class Solution:
    def merge(self, intervals):
        a = SelectionSort()
        a.selectionSort(intervals,len(intervals))
        i = 0
        while(i<len(intervals)-1):
            if intervals[i][1] >= intervals[i+1][0] and intervals[i][1] <= intervals[i+1][1]  :
                temp = intervals.pop(i+1)
                intervals[i] = [intervals[i][0], temp[1]]
                i-=1
            elif  intervals[i+1][1] <= intervals[i][1] and intervals[i+1][0] >= intervals[i][0]:
                intervals.pop(i+1)
                i-=1
            i+=1
        return intervals