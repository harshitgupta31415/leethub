class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod=10**9+7
        even=1
        odd=0
        ans=0
        sum=0
        for i in arr:
            sum= (sum+i)%2
            if sum==1:
                ans=(ans+even)%mod
                odd+=1
            else:
                ans=(ans+odd)%mod
                even+=1
        return ans