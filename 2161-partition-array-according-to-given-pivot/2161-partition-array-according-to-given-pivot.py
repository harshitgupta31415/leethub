class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less,equal,bigger=[],[],[]
        for i in nums:
            if i<pivot:
                less.append(i)
            elif i>pivot:
                bigger.append(i)
            else:
                equal.append(i)
        return less+equal+bigger
