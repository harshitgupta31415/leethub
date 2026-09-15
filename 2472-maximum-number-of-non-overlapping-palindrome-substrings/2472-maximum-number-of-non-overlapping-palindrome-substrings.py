class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        count, last_end = 0, -1

        for center in range(2 * n - 1):
            l = center // 2
            r = l + center % 2

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k and l > last_end:
                    count += 1
                    last_end = r
                    break
                l -= 1
                r += 1

        return count