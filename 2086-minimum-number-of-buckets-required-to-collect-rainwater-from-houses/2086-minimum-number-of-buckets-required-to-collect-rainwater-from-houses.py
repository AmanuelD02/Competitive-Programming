class Solution:
    def minimumBuckets(self, street: str) -> int:
        bucket = 0
        street = [ x for x in street]
        for i, block in enumerate(street):
            if block == 'H':
                if i > 0 and street[i-1] =="B":
                    continue
                
                if i + 1 < len(street) and street[i + 1] == '.':
                    bucket += 1
                    street[i + 1] = "B"

                elif i > 0 and  street[i - 1] == ".":
                    street[i - 1] = "B"
                    bucket += 1
                else:
                    return -1
        
        return bucket
                
                
                    
                    
                    
            
            