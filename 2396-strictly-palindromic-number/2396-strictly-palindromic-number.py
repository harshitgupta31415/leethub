class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        #we can use recursion but i can use np built in functio for it
        import numpy as np
        for i in range(2,n-1):
            if np.base_repr(n, i)!=np.base_repr(n,i)[::-1]:
                return False
        return True




