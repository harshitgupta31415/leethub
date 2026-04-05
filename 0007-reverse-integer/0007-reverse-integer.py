class Solution:
    def reverse(self, x: int) -> int:
        
        s=str(x)
        if s[0]=="-":
            neg=True
            s=s[1:]
        else:
            neg=False
        x= int(s[::-1])* -1 if neg else int(s[::-1])
        if x>2147483647 or x<-2147483648 :
            return 0
        return x