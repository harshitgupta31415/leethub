class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[0]*len(nums)
        rightsum=[0]*len(nums)
        ans=[]
        for i in range(1,len(nums)):
            leftsum[i]+=leftsum[i-1]+nums[i-1]
            rightsum[-i-1]+=rightsum[-i]+nums[-i]
        for i in range(len(leftsum)): ans.append(abs(leftsum[i]-rightsum[i]))
        return ans 