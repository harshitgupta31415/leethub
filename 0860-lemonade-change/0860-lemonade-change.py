class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in bills:
            if i == 10:
                five -= 1
                ten += 1
            elif i == 20:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            else:
                five += 1
            if five < 0 or ten < 0:
                return False
        return True
