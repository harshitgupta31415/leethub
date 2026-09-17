class Solution:
    def minimumChairs(self, s: str) -> int:
        ans=0
        l=[]
        for char in s:
            if char=='E':
                l.append("E")
                ans=max(ans,len(l))
            else:
                l.pop()
        return ans