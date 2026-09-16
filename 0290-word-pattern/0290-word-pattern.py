class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d=dict()
        s=s.split()
        j=0
        if len(s)!=len(pattern):
            return False
        for i in pattern:
            if i not in d:
                d[i]=s[j]
            else:
                if d[i]!=s[j]:
                    return False
            j+=1
        if len(d.values())!=len(set(d.values())):
            return False
        return True
