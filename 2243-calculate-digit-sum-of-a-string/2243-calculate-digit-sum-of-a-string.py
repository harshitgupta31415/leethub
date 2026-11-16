class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            temp = []
            i = 0
            while i < len(s):
                group = s[i:i+k]
                sum1 = sum(int(x) for x in group)
                temp.append(str(sum1))
                i += k
            s = "".join(temp)
        return s