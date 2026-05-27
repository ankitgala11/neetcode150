class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        rev = str(b)[::-1]
        rev+="0"*(32-len(rev))
        return int(rev, 2)

     