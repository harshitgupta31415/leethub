class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l=sentence.split()
        s=len(searchWord)
        for i in range(len(l)):
            if l[i][:s] == searchWord: 
                return i+1
        return -1