class Solution:
    def myAtoi(self, s: str) -> int:
        if s=="":
            return 0
        s=s.split()[0]
        s+="a"
        if s[0]=="-":
            neg=True
            s=s[1:]
        elif s[0]=="+":
            neg=False
            s=s[1:]
        else:
            neg=False
        for i in range(len(s)):
            if not s[i].isdigit():
                s=s[:i]
                break
        if s=="":
            return 0
        s=int(s)
        if neg:
            s*=-1
        if s >= 2147483647:
            return 2147483647
        elif s<=-2147483648:
            return -2147483648
        return s