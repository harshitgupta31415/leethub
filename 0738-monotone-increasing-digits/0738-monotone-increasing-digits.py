class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        k=str(n)
        l=list(k)
        c=len(l)
        for i in range(len(l)-1,0,-1):
            if l[i-1]>l[i]:
                l[i-1]=str(int(l[i-1])-1)
                c=i
        for i in range(c,len(k)):
            l[i]='9'
        return int("".join(l))