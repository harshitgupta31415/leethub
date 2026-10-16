class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        pos={}
        oe={"odd":0,"even":0}
        for i in position:
            pos[i]=pos.get(i,0)+1
        for j in pos:
            if j%2==0:
                oe["even"]+=pos[j]
            else:
                oe["odd"]+=pos[j]
        return min(oe.values())