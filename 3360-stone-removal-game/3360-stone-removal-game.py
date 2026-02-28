class Solution:
    def canAliceWin(self, n: int) -> bool:
        ans=False
        i=10
        while i<=n:
            n-=i
            i-=1
            if ans==True:
                ans=False
            else:
                ans=True
        return ans 