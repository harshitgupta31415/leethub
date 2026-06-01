class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        mx=0
        n=len(nums)
        for i in range(len(nums)):
            mx=max(mx,abs(nums[i]-nums[(i+1)%n]))
        return mx