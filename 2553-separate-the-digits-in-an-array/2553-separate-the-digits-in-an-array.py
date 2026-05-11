class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            if i<10:
                ans.append(i)
            else:
                for j in str(i):
                    ans.append(int(j))
        return ans