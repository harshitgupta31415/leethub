class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        h={0:0}
        res=0
        for i in hours:
            r =i%24
            if r==0:
                res+=h[r]
            else:
                if 24 - r in h:
                    res+=h[24-r]
            if r in h:
                h[r]+=1
            else:
                h[r]=1
        return res