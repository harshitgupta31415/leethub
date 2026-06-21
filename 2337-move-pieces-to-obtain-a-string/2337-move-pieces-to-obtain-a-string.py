class Solution:
    def canChange(self, start: str, target: str) -> bool:
        new_start = start.replace("_", "")
        new_target = target.replace("_", "")
        if new_start != new_target:
            return False
        i = j = 0
        while i < len(start) and j < len(target):
            if start[i] == "_":
                i += 1
                continue
            if target[j] == "_":
                j += 1
                continue
            if (start[i] == "L" and i < j) or (start[i] == "R" and i > j):
                return False
            i += 1
            j += 1
        return True