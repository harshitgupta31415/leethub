class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        fives=5
        ans=0
        k = int(log(n, 5))
        for i in range(k):
            count = n // fives
            ans+= count
            fives*= 5
        return ans
    