class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def maxans(nums):
            ans=1
            curr=1
            for i in range(len(nums)-1):
                if nums[i]< nums[i+1]:
                    curr+=1
                else:
                    curr=1
                ans=max(curr,ans)
            return ans
        return max(maxans(nums),maxans(nums[::-1]))