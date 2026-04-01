class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        res= "Bob" if min(x,y//4)%2==0  else "Alice"
        return res