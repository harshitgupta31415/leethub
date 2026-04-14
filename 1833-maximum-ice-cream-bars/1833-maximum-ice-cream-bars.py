class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans=0
        for i in sorted(costs):
            if i<=coins:
                ans+=1
                coins-=i
        return ans