class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=0
        mx=0
        for i in nums:
            a=max(mx,prev+i)
            prev,mx=mx,a
        return mx

