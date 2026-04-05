class Solution:
    def reverse(self, x: int) -> int:
        
        neg=x<0
        ans=int(str(abs(x))[::-1])*-1
        if neg:
            return ans if ans>-2147483648 else 0
        else:
            return ans*-1 if  ans>-2147483647 else 0