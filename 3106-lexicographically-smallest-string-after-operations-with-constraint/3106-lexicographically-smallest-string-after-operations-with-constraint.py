class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        res = list(s)
        for i, c in enumerate(s):
            d1 = ord(c) - ord('a')
            d2 = 26 - d1
            cost = min(d1, d2)
            if k >= cost:
                res[i] = 'a'
                k -= cost
            else:
                res[i] = chr(ord('a') + (d1 - k))
                k = 0
                break
        return ''.join(res)