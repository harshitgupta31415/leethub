class Solution:
    def canAliceWin(self, n: int) -> bool:
        ans,i=0,10
        while i<=n:
            n-=i
            i-=1
            ans^=1
        return ans==1