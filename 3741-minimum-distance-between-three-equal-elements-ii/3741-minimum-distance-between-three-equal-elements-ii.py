class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = {}

        for i in range(len(nums)):
            if nums[i] not in pos:
                pos[nums[i]] = []
            pos[nums[i]].append(i)
        
        dist = float('inf')
        
        for points in pos.values():
            if len(points) < 3:
                continue
            
            for i in range(len(points) - 2):
                dist = min(dist, 2 * (points[i+2] - points[i]))
        
        return dist if dist != float('inf') else -1
        
        """
        from collections import Counter
        
        count = Counter(nums)
        digit = set()
        
        for i in count:
            if count[i] >= 3:
                digit.add(i)
        
        if len(digit) == 0:
            return -1
        
        dist = float('inf')
        l = []
        
        for j in digit:
            points = []
            for i in range(len(nums)):
                if nums[i] == j:
                    points.append(i)
            l.append(points)
        
        for points in l:
            for i in range(len(points) - 2):
                dist = min(dist, 2 * (points[i+2] - points[i]))
        
        return dist
        """