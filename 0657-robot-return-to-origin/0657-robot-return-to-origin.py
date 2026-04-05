class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter
        moves=Counter(moves)
        return moves["U"]==moves["D"] and moves["L"]==moves["R"]