class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        up="."*n
        right="#"*(n-1)+"."
        return [up]+[right]*(m-1)