class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        nums=Counter(nums)
        for i in nums:
            if i%2==0 and nums[i]==1:
                return i
        return -1