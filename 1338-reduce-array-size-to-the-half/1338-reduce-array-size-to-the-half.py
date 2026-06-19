class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter, target = Counter(arr), len(arr) / 2
        total = 0
        for index, val in enumerate(sorted(counter.values(), reverse=True)):
            total += val
            if total >= target:
                return index + 1