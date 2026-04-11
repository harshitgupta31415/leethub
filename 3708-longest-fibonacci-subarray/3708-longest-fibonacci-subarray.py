class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=0
        l=nums[:2]
        for i in range(2,len(nums)):
            if nums[i-2]+nums[i-1]==nums[i]:
                l.append(nums[i])
            else:
                l=nums[i-2:i]
            ans=max(ans,len(l))
            if ans+i-len(l)>len(nums):
                break
        return ans