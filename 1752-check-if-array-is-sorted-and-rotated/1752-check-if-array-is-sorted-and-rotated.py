class Solution:
    def check(self, nums: List[int]) -> bool:
        st=nums[0]
        dip=False
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%len(nums)] :
                if dip:
                    return False
                else:
                    dip=True
        return True

        #same but efficient readability
        """
        st=nums[0]
        dip=False
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1] :
                if dip:
                    return False
                else:
                    dip=True
        if dip:
            if nums[-1]<=st:
                return True
            else:
                return False
        return True

        """

