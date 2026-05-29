class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')
        for i in nums:
            total = 0
            while i > 0:
                total += (i % 10)
                i //= 10
            ans = min(ans, total)
        return ans