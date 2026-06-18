class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outer = [[]]
        for i in nums: 
            for j in range(len(outer)):
                internal = outer[j] + [i]
                outer.append(internal)
        return outer