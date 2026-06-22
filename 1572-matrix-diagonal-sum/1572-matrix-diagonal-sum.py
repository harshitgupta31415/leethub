class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans=0
        if len(mat)%2==1:
            ans-=mat[len(mat)//2][len(mat)//2]
        for i in range(len(mat)):
            ans+=mat[i][i]
        for i in range(1,1+len(mat)):
            ans+=mat[i-1][-i]
        return ans