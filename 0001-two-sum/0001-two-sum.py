class Solution:
    def twoSum(self, nums, t):
        copy=nums[:]
        nums.sort()
        l=0
        r=len(nums)-1
        while l<r:
            sm=nums[l]+nums[r]
            if sm<t:
                l+=1
            elif sm>t:
                r-=1
            else:
                break
        if nums[l]==nums[r]:
            l=copy.index(nums[l])
            r=len(copy)-copy[::-1].index(nums[r]) -1
            return [l,r]
        return [copy.index(nums[l]),copy.index(nums[r])]