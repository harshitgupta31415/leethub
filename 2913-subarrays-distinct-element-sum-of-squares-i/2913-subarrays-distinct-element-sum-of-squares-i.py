class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        for l in range(n):
            s = set()
            for r in range(l, n):
                s.add(nums[r])
                ans += len(s)**2
        return ans