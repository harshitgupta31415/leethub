class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_val=0
        nums.sort()
        for i in range(len(nums)):
            if i<len(nums)-1 and nums[i+1]-nums[i]>max_val :
                max_val=nums[i+1]-nums[i]
        return max_val