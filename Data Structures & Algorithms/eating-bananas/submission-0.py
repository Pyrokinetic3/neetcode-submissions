class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        min_rate = 1
        while min_rate <= max_rate:
            k = (max_rate + min_rate) // 2
            t = sum(((p + k - 1) // k) for p in piles)
            if t <= h:
                max_rate = k - 1
            else:
                min_rate = k + 1
        return min_rate