class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        for bit in range(32):
            count = 0
            for num in nums:
                if num & (1 << bit):
                    count += 1
            if count >= k:
                ans |= (1 << bit)
        return ans