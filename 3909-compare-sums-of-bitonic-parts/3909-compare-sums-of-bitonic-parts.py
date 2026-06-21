class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        i=nums.index(max(nums))
        asc=sum(nums[:i])
        desc=sum(nums[i+1:])
        if asc>desc:
            return 0
        elif asc<desc:
            return 1
        return -1