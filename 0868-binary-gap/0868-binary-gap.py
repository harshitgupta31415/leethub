class Solution:
    def binaryGap(self, n: int) -> int:
        maxi = 0
        bn = bin(n)[2:]
        i=0
        j=1
        while(j<len(bn)):
            if(bn[i]=='1' and bn[j]=='1'):
                maxi = max(maxi,j-i)
                i=j
            j+=1
        return maxi
        