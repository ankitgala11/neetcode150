class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [i.lower() for i in s if i.isalnum() ]
        print(arr)
        return arr == arr[::-1]