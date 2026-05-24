class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mn = min(len(word1), len(word2))
        ans = []
        for i in range(mn):
            ans.append(word1[i])
            ans.append(word2[i])
        ans.append(word1[mn:])
        ans.append(word2[mn:])
        
        return "".join(ans)
        
        """
        m,n=len(word1),len(word2)
        ans=''
        if m>=n:
            for i in range(n):
                ans+=word1[i]+word2[i]
            return ans+word1[n:]
        else:
            for i in range(m):
                ans+=word1[i]+word2[i]
            return ans+word2[m:]
        """