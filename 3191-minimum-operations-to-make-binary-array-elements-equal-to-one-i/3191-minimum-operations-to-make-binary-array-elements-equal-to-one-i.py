class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l=0
        count=0
        r=3
        for j in range(len(nums) - 2):
            if nums[l]!=1:
                count+=1
                for i in range(l,l+3):
                    nums[i]=abs(nums[i]-1)
            l+=1
        return count if 0 not in nums else -1
        