class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        r=[0]*len(heights)
        s=[]
        for i in range(len(heights)-1,-1,-1):
            while len(s)>0 and heights[i]>s[-1]:
                r[i]+=1
                s.pop()
            if len(s)>0:
                r[i]+=1
            s.append(heights[i])
        return r
