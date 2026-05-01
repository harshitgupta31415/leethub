class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        sum = 0
        F = 0
        for i in range(len(nums)):
            sum += nums[i]
            F += i * nums[i]
        result = F
        for k in range(1, len(nums)):
            F=F+sum-len(nums)*nums[len(nums)-k]
            result=max(result,F)
        return result