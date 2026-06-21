class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mx1=0
        mx2=0
        sum1=0
        sum2=0
        for u in nums:
            sum1+=u
            sum2+=u
            mx1=max(mx1,sum1)
            mx2=min(mx2,sum2)
            if(sum1<0):
                sum1=0
            if(sum2>0):
                sum2=0
        
        return max(mx1,abs(mx2))