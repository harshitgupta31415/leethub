class Solution:
    def maxBottlesDrunk(self, numBottles: int, numEx: int) -> int:
        total=numBottles
        while(numBottles>=numEx):
            numBottles-=numEx-1
            numEx+=1
            total+=1
        return total
        
   
"""
        drink=0
        empty=0
        print(numBottles,empty,numEx,drink)
        while True:
            if numBottles>0:
                drink+=numBottles
                empty+=numBottles
                numBottles=0
            else:
                break
            while empty>=numEx:
                numBottles+=1
                empty-=numEx
                numEx+=1
        return drink

"""