class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count=Counter(nums)
        res = 0
        for i in count.keys():
            if i == 1:
                total = count[i] if count[i] % 2 else count[i] - 1
            else:
                total = 0
                while count[i] >= 2 and i**2 in count:
                    total += 2
                    i**=2
                total += 1
            res = max(res, total)
        return res