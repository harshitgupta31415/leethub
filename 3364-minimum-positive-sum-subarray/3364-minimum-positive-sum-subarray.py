class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans=float('inf')
        x=l
        for j in range(x,r+1):
            l=j
            sum=0
            for i in range(len(nums)):
                sum+=nums[i]
                if i>=l:
                    sum-=nums[i-l]
                if sum>0 and i>= l-1:
                    ans=min(ans,sum)
        return ans if ans!=float('inf') else -1