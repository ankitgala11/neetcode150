class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits.reverse()
        n = len(digits)

        carry = 1
        for i in range(n):
            temp = carry + digits[i]
            digits[i] = temp%10
            carry = temp//10
        
        if carry:
            digits.append(carry)
        
        digits.reverse()
        return digits
