class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:       
        l=0
        r=0
        bigstr=""
        while r<len(s):
            news=s[l:r+1]
            if len(news) != len(set(news)):
                l+=1
            else:
                if len(news)>len(bigstr):
                    bigstr=news
                r+=1
        
        return len(bigstr)