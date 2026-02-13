class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenl=[]
        oddl=[]
        for i in nums:
            if i%2==0:
                evenl.append(i)
            else:
                oddl.append(i)
        evenl.sort()

        return evenl+oddl