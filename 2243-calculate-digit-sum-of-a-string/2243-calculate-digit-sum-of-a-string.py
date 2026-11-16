class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            temp = []
            i = 0
            while i < len(s):
                group = s[i:i+k]
                sum_val = sum(int(ch) for ch in group)
                temp.append(str(sum_val))
                i += k
            s = "".join(temp)
        return s