class Solution:
    def minOperations(self, nums: List[int]) -> int:
        x=nums[len(nums)-1]
        ans=0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>x:
                for j in range(2,int(nums[i]**0.5)+1):
                    if nums[i]%j==0:
                        nums[i]=j
                        ans+=1
                        break
            if nums[i]>x:
                return-1
            x=nums[i]
        return ans