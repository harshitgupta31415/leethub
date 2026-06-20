class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        empties = 0
        while numBottles > 0:
            total += numBottles
            numBottles, empties = divmod(numBottles + empties, numExchange)
        return total