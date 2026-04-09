class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        i,j,count=0,0,0
        while i<len(nums)-1:
            if nums[i]==nums[i+1] and (i+j)%2==0:
                j-=1
                count+=1
            i+=1
        return count+1 if (len(nums)-count) %2!=0 else count