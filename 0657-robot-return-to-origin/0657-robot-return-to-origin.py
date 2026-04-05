class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter
        moves=dict(Counter(moves))
        try:
            if "U" not in moves and "D" not in moves or moves["U"]==moves["D"] :
                if "L" not in moves and "R" not in moves or moves["L"]==moves["R"]:
                    return True
            return False
        except:
            return False