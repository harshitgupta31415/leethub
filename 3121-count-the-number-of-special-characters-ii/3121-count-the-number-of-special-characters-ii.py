class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small=set()
        ans=0
        removed=set()
        caps=set()
        for i in range(len(word)):
            if word[i]!=word[i].upper():
                if word[i].upper() not in caps:
                    small.add(word[i])
                else:
                    removed.add(word[i])             
            elif word[i]==word[i].upper():
                caps.add(word[i])
        match=set()
        for i in small:
            if i.upper() in caps:
                ans+=1
                match.add(i)
        for i in removed:
            if i in match:
                ans-=1
        return ans