class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        st = "11"

        for _ in range(n - 2):
            count = 1
            s = ""

            j = 0
            while j < len(st) - 1:
                if st[j] == st[j + 1]:
                    count += 1
                else:
                    s += str(count)
                    s += st[j]
                    count = 1
                j += 1

            s += str(count)
            s += st[j]
            st = s

        return st