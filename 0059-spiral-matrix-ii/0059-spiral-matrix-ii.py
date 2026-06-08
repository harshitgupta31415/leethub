class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rows = n
        cols = n

        mat= [[0] * n for i in range(0, n)]
        
        i= 0
        j= 0
        cnt = 0
        wall = 0
        total_ele = n * n
        curr = 1
        
        while cnt < total_ele:
            while cnt < total_ele and j < cols - wall:
                cnt += 1
                mat[i][j] = curr 
                curr += 1
                j += 1
            
            j -= 1
            i += 1

            while cnt < total_ele and i < rows - wall:
                cnt += 1
                mat[i][j] = curr 
                curr += 1
                i += 1

            i -= 1
            j -= 1

            while cnt < total_ele and j >= wall:
                cnt += 1
                mat[i][j] = curr 
                curr += 1
                j -= 1

            j += 1
            i -= 1

            while cnt < total_ele and i > wall:
                cnt += 1
                mat[i][j] = curr 
                curr += 1
                i -= 1

            i += 1
            j += 1
            wall += 1
                
        return mat