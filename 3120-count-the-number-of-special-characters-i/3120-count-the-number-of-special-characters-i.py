class Solution:
    def numberOfSpecialChars(self, w: str) -> int:
        wset=set(w)
        ans=0
        for i in w:
            if i.upper()!=i and i.upper() in wset:
                ans+=1
                wset.remove(i)
                wset.remove(i.upper())
        return ans