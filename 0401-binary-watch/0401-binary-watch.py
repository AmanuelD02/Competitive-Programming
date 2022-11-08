class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        lst = ['0'] * 10
        self.validTimes = []
        
        self.backtrack(0, turnedOn, lst)
        
        return self.validTimes
        
    def backtrack(self, i, led, lst):
        if led == 0:
            isValid = self.validate(lst)
            
            if isValid != None:
                self.validTimes.append(isValid)
            return
        
        if i == 10:
            return
        
        
        lst[i] = '1'
        self.backtrack(i+1, led - 1, lst)
        
        lst[i] = '0'
        self.backtrack(i+1, led, lst)
        
        
            
    
    def validate(self, lst):
        hour = int(''.join(lst[:4]), 2)
        minutes = int(''.join(lst[4:]), 2)
        
        if 0 <= hour <12 and 0 <= minutes <60:
            ans = self.converter(hour, minutes)

            return ans
        
        return None 
            
    
    def converter(self, hour, minutes):        
        ans = []
            
        ans.append(str(hour))
        ans.append(':')
        
        if minutes < 10:
            ans.append('0')
        ans.append(str(minutes))
        return "".join(ans)
        