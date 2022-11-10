class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        
        for i in range(n-1,-1,-1):
            if digits[i] + carry == 10:
                digits[i] = 0
            else:
                digits[i]  = digits[i] + carry
                carry = 0
                break
        
        if i == 0 and carry:
            digits.insert(0, carry)
        
        
        return digits