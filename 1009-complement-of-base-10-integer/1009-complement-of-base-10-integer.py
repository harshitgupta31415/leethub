class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n1=bin(n)[2:]
        n=''
        for i in n1:
            if i =="1":
                n +="0"
            else:
                n +="1"
        return int(n,2)