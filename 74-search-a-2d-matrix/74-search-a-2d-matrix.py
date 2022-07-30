class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left , right = 0, len(matrix)-1
        while left <=right:
            mid = (left + right)//2
            ary = matrix[mid]
            if ary[0] <= target <= ary[-1]:
                # another binary search
                left , right = 0, len(ary)-1
                while left <=right:
                    mid = (left+ right) //2
                    val = ary[mid]
                    if val ==target:
                        return True
                    elif target > val:
                        left = mid +1
                    else:
                        right= mid -1
                return False
                
            elif target >ary[-1]:
                left = mid +1
            else:
                right = mid -1
                
        
        return False