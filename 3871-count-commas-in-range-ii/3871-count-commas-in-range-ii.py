class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        i = 1  
        while True:
            start = 10 ** (3 * i)               
            if n < start:
                break
            end = min(n, 10 ** (3 * (i + 1)) - 1) 
            ans += (end - start + 1) * i
            i += 1
        return ans