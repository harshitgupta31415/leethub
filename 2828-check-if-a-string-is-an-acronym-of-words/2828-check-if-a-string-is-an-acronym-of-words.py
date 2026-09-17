class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        letter = ""
        for i in range(len(words)):
            letter += words[i][0]
        return letter == s