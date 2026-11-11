class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans=need1*cost1+need2*cost2
        if cost1+cost2>costBoth:
            common=min(need1,need2)
            ans=min(ans,common*costBoth+(need1-common)*cost1+(need2-common)*cost2)
        ans=min(ans,max(need1,need2)*costBoth)
        return ans