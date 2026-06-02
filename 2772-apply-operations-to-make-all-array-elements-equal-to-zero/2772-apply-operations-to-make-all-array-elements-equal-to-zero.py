class Solution:
    def checkArray(self, A: List[int], k: int) -> bool:
        cur = 0
        for i, a in enumerate(A):
            if cur > a:
                return False
            A[i], cur = a - cur, a
            if i >= k - 1:
                cur -= A[i - k + 1]
        return cur == 0
        