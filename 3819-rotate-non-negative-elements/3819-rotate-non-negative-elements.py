class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        l=[]
        pos=[]
        for i in range(len(nums)):
            if nums[i]>=0:
                l.append(nums[i])
                pos.append(i)
        k=k%len(l) if len(l)!=0 else 0
        l=l[k:]+l[:k]
        for i in range(len(pos)):
            nums[pos[i]],l[i]=l[i],nums[pos[i]]
        return nums