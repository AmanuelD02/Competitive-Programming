class Solution:
    def numberToWords(self, num: int) -> str:
        toNineteen = {0:"", 1:"One", 
                      2:"Two", 3:"Three",
                      4:"Four", 5:"Five", 
                      6:"Six", 7:"Seven",
                      8:"Eight", 9:"Nine", 
                      10:"Ten", 11:"Eleven", 
                      12:"Twelve", 13:"Thirteen", 
                      14:"Fourteen", 15:"Fifteen",
                      16:"Sixteen", 17:"Seventeen", 
                      18:"Eighteen", 19:"Nineteen"}
        
        nums = [20, 100, 1000, 1000000, 1000000000]             
        
        toNinety = ["", "", "Twenty",
                    "Thirty", "Forty", "Fifty",
                    "Sixty", "Seventy",
                    "Eighty", "Ninety"]
   
        def helper(num):
            curr = ""
            if num < nums[0]:
                curr = toNineteen[num]
                
            elif num < nums[1]:
                curr = toNinety[num // 10] + " " + toNineteen[num % 10]
                
            elif num < nums[2]:
                curr = helper(num // 100) + " Hundred " + helper(num % 100)
                
            elif num < nums[3]:
                curr = helper(num // 1000) + " Thousand " + helper(num % 1000)
                
            elif num < nums[4]:
                curr = helper(num // 1000000) + " Million " + helper(num % 1000000)
                
            else:
                curr = helper(num // 1000000000) + " Billion " + helper(num % 1000000000)
                
            curr = curr.strip()
            return  curr
        
        return helper(num) or "Zero"