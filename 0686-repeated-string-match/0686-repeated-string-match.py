class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        import math
        ans=math.ceil((len(b)/len(a)))
        s=a*ans
        if b in s:
            return ans
        else:
            s+=a
            if b in s:
                return ans+1
            return -1