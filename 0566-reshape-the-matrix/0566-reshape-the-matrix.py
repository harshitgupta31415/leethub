class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0])!=r*c:
            return mat
        l=[]
        ans=[]
        for i in mat:
            l+=i
        for i in range(r):
            ans.append(l[c*i:c*(i+1)])
        return ans
