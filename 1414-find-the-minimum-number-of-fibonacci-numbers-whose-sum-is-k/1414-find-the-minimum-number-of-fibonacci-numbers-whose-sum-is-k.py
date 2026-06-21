class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib=[0, 1]
        while fib[-1]<=k:
            fib.append(fib[-1]+fib[-2])
        ans=0
        for i in reversed(fib):
            while i<=k:
                k-=i
                ans+=1
            if k==0:
                break
        return ans