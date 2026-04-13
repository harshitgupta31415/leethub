class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        from collections import Counter
        l=list(Counter(tasks).values())
        print(l)
        if 1 in l:
            return -1
        ans=0
        for i in l:
            ans+=i//3
            i%=3
            if i==1:
                i+=3
                ans-=1
            ans+=i//2
            i%=2
        return ans