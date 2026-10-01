class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{": "}", "[": "]"}
        newl = []       
        for char in s:
            if char in d:
                newl.append(char)
            else:
                if not newl or char != d[newl[-1]]:
                    return False
                newl.pop()
        return len(newl) == 0