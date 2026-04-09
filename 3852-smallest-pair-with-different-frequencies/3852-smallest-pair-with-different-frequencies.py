class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq={}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        values=list(freq.keys())
        values.sort()
        n=len(values)
        for i in range(n-1):
            x=values[i]
            for j in range(i+1,n):
                y=values[j]
                if freq[x]!=freq[y]:
                    return [x,y]
        return [-1,-1]