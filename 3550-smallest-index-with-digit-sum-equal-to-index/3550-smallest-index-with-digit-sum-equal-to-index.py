class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        if nums[0]==0:
            print(nums[0])
            return 0
        for i in range(len(nums)):
            sum=0
            while nums[i]>0:
                sum+=nums[i]%10
                nums[i]//=10
            if sum==i:
                print(sum,i)
                return i
        return -1