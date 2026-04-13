class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even = (n + 1) // 2
        odd = n // 2
        return (pow(5, even, mod) * pow(4, odd, mod)) % mod
        
        '''
        if n%2==0:
            e=n/2
            o=n/2
        else:
            e=n//2+1
            o=n//2
        return ((5**e)*(4**o))%(1000000007)
        '''