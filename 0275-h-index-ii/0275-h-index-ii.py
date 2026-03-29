class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l = 0
        r = n
        while l < r:
            m = (l + r + 1) // 2
            if citations[n - m] >= m:
                [l, r] = [m, r] 
            else:
                [l, r] = [l, m - 1]
        return l
