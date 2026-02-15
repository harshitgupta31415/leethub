class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec_a=0
        dec_b=0
        k=0
        bin_sum=0
        for i in range(0,len(a)):
            dec_a+=int(a[i])*(2**(len(a)-1-i))
        for i in range(0,len(b)):
            dec_b+=int(b[i])*(2**(len(b)-1-i))     
        sum=dec_a+dec_b
        while sum>0:
            bin_sum+=(sum%2)*(10**k)
            k+=1
            sum//=2
        return str(bin_sum)