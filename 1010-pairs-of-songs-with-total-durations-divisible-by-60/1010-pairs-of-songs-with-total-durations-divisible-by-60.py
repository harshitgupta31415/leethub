class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders=[0]*60
        for i in time:
            remainders[i%60]+=1
        count=0
        count+=remainders[0]*(remainders[0]-1)//2
        count+=remainders[30]*(remainders[30]-1)//2
        for i in range(1,30):
            count+=remainders[i]*remainders[60-i]
        return count