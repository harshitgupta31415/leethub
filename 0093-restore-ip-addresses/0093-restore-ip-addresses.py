class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        def f(i, r, d):
            if i == n and d == 4:
                ans.append(r[:-1])
                return
            if i >= n or d == 4:
                return
            if s[i] == "0":
                f(i + 1, r + "0.", d + 1)
                return
            for j in range(1, 4):
                p = s[i:i + j]
                if int(p) > 255:
                    break
                f(i + j, r + p + ".", d + 1)
        f(0, "", 0)
        return ans    