class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:       
        l=0
        r=0
        bigstr=""
        seen=set()
        length=0
        while r<len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                if len(seen)>length:
                    length=len(seen)
            else:
                seen.remove(s[l])
                l+=1
        return length