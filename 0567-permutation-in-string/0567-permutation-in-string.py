class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        l=0
        counters1=Counter(s1)
        for r in range(len(s1),len(s2)+1):
            
            if Counter(s2[l:r])==counters1:
                return True
            l+=1
        return False