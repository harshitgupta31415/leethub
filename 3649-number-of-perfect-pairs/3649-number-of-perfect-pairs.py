class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        nums=[abs(i) for i in nums]
        nums.sort()
        i=len(nums)-1
        j=len(nums)-2
        ans=0
        while i>=0:
            while j>=0 and nums[i]-nums[j]<=nums[j]:
                j-=1
            ans+=i-j-1
            i-=1
        return ans