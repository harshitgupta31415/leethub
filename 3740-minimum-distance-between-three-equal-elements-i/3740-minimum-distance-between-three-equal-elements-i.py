class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        indices_map = defaultdict(list)
        
        for i, num in enumerate(nums):
            indices_map[num].append(i)
            
        min_dist = float('inf')
        
        for indices in indices_map.values():
            if len(indices) >= 3:
                for j in range(len(indices) - 2):
                    dist = 2 * (indices[j + 2] - indices[j])
                    if dist < min_dist:
                        min_dist = dist
                        
        if min_dist != float('inf'):
            return min_dist
        else:
            return -1