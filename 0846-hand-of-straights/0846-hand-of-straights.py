from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for num in sorted(count.keys()):
            size = count[num]
            if size == 0:
                continue
            for i in range(num, num + groupSize):
                count[i] -= size
                if count[i] < 0:
                    return False
        return True