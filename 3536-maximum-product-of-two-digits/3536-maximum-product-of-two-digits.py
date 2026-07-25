class Solution:
    def maxProduct(self, n: int) -> int:
        n=str(n)
        l=[]
        for i in n:
            l.append(i) 
        l.sort()
        return int(l[-1])*int(l[-2])