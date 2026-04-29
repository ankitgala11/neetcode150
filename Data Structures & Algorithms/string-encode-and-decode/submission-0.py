class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            for ch in word:
                encoded += str(ord(ch))
                encoded += '#'
            encoded += "*"

        return encoded

    def decode(self, s: str) -> List[str]:

        original = []
        n = len(s)
        temp = ""
        word = ""

        for i in s:
            if i == "#":
                word += chr(int(temp))
                temp = ""
                
            
            elif i == "*":
                print(word)
                original.append(word)
                word = ""

            else:
                temp += str(i)
        
        return original

