class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = Trie()
            curr=curr.children[i]
        curr.isEnd=True
        

    def search(self, word: str) -> bool:

        curr = self.root

        def solve(curr, i):
            if i==len(word):
                return curr.isEnd
            
            # if i == len(word)-1:
            #     if word[i] in curr.children and curr.children[word[i]].isEnd or word[i]=='.' and:
            #         return True
            #     return False
            
            if word[i] in curr.children:
                if solve(curr.children[word[i]], i+1):
                    return True
            elif word[i] == '.':
                for char in curr.children.keys():
                    if solve(curr.children[char], i+1):
                        return True
                return False

            return False


        return solve(curr, 0)

  
        


