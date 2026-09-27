class Solution:
    def reverseParentheses(self, s: str) -> str:
        l=[]
        ans=""
        for i in range(len(s)):
            if s[i]=="(":
                l.append(ans)
                ans=""
            elif s[i]==")":
                ans=ans[::-1]
                ans=l.pop()+ans
            else:
                ans+=s[i]
        return ans