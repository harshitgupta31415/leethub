class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero=0 in nums
        prod=1
        ans=[]
        if not zero:
            for i in nums:
                prod*=i
            for i in nums:
                ans.append(int(prod/i))
        else:
            count_zero=nums.count(0)
            if count_zero>1:
                return [0]*len(nums)
            else:
                for i in nums:
                    if i!=0:
                        prod*=i
                for i in nums:
                    if i!=0:
                        ans.append(0)
                    else:
                        ans.append(prod)
        return ans