class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        if k==1:
            return grid
        relevent=[]
        for i in range(x,x+k):
            relevent.append(grid[i][y:y+k])
        ans=[]
        for i in relevent[::-1]:
            ans.append(i)
        for i in range(x):
            ans.insert(i,grid[i])
        
        for i in range(x+k,len(grid)):
            ans.insert(i,grid[i])
        for i in range(x,x+k):
            ans[i]=grid[i][0:y]+ans[i]+grid[i][y+k:]
        return ans