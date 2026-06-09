class Solution:
    def maxFreqSum(self, s: str) -> int:
        vov=""
        const=""
        for i in s:
            if i in "aeiou":
                vov+=i
            else:
                const+=i
        vov=Counter(vov)
        const=Counter(const)
        ans=0
        if vov:
            ans+=max(vov.values())
        if const:
            ans+=max(const.values())
        return ans