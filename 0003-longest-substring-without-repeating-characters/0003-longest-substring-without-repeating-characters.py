class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,r=0,1
        mx,curr=0,0
        while  r<=len(s)-1:
            if len(s[l:r])==len(set(s[l:r])):
                curr=len(s[l:r])
                r+=1
            else:
                mx=max(mx,curr)
                l+=1
                r+=1
        if len(s[l:r])==len(set(s[l:r])):
            curr+=1
        return max(mx,curr)