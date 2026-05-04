class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
# Do not return anything, modify matrix in-place instead.
        l=[]
        for i in range(len(matrix)):
            l+=[[]]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                l[j].append(matrix[-1-i][j])
        matrix[:]=l