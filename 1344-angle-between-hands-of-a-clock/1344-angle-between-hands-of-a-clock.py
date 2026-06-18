class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m_angle = 6.0 * minutes
        h_angle = 30.0 * (hour % 12) + 0.5 * minutes

        diff = abs(h_angle - m_angle)

        return min(diff, 360.0 - diff)