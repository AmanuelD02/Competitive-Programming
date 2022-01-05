# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lst  = []
        
        TL = 0
        TR = len(matrix[0]) 
        BR = len(matrix) 
        BL = 0
        
        while( TL < BR and BL < TR):
            for i in range(BL, TR):
                
                lst.append( matrix[TL][i])
            TL +=1
            
            for i in range( TL, BR):
                
                lst.append(matrix[i][TR-1])
            TR -=1
            
            if not (BL < TR and TL < BR):
                break
            for i in range(TR-1,BL-1,-1 ):
                
                lst.append(matrix[BR-1][i])
            BR-=1
            
            for i in range(BR-1,TL-1,-1 ):
                
                lst.append( matrix[i][BL])
            BL +=1
            
            # print(TL,TR,BR,BL)
  
            
        return lst
        