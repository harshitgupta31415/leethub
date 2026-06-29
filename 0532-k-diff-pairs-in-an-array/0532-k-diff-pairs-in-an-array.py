class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            res = 0
            c = Counter(nums)
            for i in c:
                if c[i] > 1:
                    res += 1
            return res
        s = set(nums)
        res = 0
        for i in s:
            if i + k in s:
                res += 1
        return res