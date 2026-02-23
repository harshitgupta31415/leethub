class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        maxcount=0
        def findbomb(n,seen):
            count=0
            for i in range(len(bombs)):
                xdiff=bombs[n][0]-bombs[i][0]
                ydiff=bombs[n][1]-bombs[i][1]
                if i not in seen and xdiff*xdiff + ydiff*ydiff <= bombs[n][2] * bombs[n][2]:
                    seen.add(i)
                    count+=1+findbomb(i,seen)
            return count


        for i in range(len(bombs)):
            count=0
            seen=set()
            seen.add(i)
            count=findbomb(i,seen)
            if count>maxcount:
                maxcount=count
        return maxcount+1