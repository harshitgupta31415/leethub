class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word=set(word)
        ans=0
        for i in word:
            if i.upper() in word and i.upper()!= i:
                ans+=1
        return ans