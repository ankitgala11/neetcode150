class Solution:
    def checkValidString(self, s: str) -> bool:
        l = 0
        st = 0 
        r = 0


        for i in s:
            if i == '(':
                l+=1
            elif i ==')':
                r+=1
            else:
                st += 1
            
            if r>l+st:
                return False

        
        a =  min(l, r)+st>=max(l, r)
        l = 0
        st = 0 
        r = 0

        for i in s[::-1]:
            if i == '(':
                l+=1
            elif i ==')':
                r+=1
            else:
                st += 1
            
            if l>r+st:
                return False

        
        b =  min(l, r)+st>=max(l, r)

        return a and b
        