class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        ans=0
        for i in range(n-1,-1,-1):
            l,r=0,i-1
            while l<r:
                if nums[l]+nums[r]>nums[i]:
                    ans+=r-l
                    r-=1
                else:
                    l+=1
        return ans