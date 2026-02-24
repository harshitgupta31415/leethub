class Solution(object):
    def generate(self, numRows):
        a=[[1]]
        for i in range(1,numRows):
            res=[1]
            for j in range(len(a[i-1])):
                try:
                    res.append(a[i-1][j]+a[i-1][j+1])
                except:
                    res.append(a[i-1][j])
            a.append(res)
        return a
            