class Solution:
    def brokenCalc(self, start: int, target: int) -> int:
        steps = 0
        while start < target:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            steps += 1
        return steps + (start - target)