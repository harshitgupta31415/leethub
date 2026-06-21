class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        k=k%((n-1)*2) 
        if k<n:
            return k
        return (n-1)*2-k