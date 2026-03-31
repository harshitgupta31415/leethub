class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels=list(set(list(jewels)))
        ans=0
        for i in jewels:
            ans+=stones.count(i)
        return ans