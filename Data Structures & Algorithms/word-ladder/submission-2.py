class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)
        if endWord not in wordSet:return 0
        n = len(wordList[0])

        q = [(beginWord, 1)]
        vis = set()
        vis.add(beginWord)

        while q:
            
            word, step = q.pop(0)
            print(word, step)

            if word == endWord:
                return step

            for i in range(n):
                temp = list(word)
                for ch in range(97, 123):
                    temp[i] = chr(ch)
                    newword = "".join(temp)


                    if newword not in vis and newword in wordSet:
                        q.append((newword, step+1))
                        vis.add(newword)
            

        return 0

