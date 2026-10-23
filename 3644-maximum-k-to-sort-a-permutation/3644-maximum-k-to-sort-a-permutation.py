class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans=-1
        if nums[0]!=0:
            return 0
        for i in range(len(nums)):
            if nums[i]!=i:
                ans&=nums[i]
        return max(ans,0)