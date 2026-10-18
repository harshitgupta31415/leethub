class Solution:
    def twoSum(self, nums, t):
        s = Counter(nums)
        for i in range(len(nums)):
            if t - nums[i] in s:
                if t==2*nums[i] and s[nums[i]]>1:
                    return [i, len(nums) - 1 - nums[::-1].index(t - nums[i])]
                elif t!=2*nums[i]:
                    return [i, nums.index(t - nums[i])]
