class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        
        for i in range(n):
            s1=s[::-1]
            s2=""
            for j in s1:
                if j =="0":
                    s2+="1"
                else:
                    s2+="0"
            s=s+"1"+s2
        return s[k-1]