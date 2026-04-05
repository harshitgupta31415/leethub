class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l=0
        count=0
        r=3
        while r<len(nums)+1:
            if nums[l]!=1:
                count+=1
                for i in range(l,l+3):
                    if nums[i]==0:
                        nums[i]=1
                    else:
                        nums[i]=0
            l+=1
            r+=1
        return count if 0 not in nums else -1
        