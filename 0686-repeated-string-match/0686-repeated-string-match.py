class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        import math
        s=a*math.ceil((len(b)/len(a)))
        print(s)
        if b in s:
            return math.ceil(len(b)/len(a))
        else:
            s+=a
            if b in s:
                return math.ceil(len(b)/len(a)+1)
            return -1