class SolutionBrute:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i,h in enumerate(height):
            left_max = 0
            j = i - 1
            while j >= 0:
                left_max = max(left_max, height[j])
                j -= 1
            right_max = 0
            j = i + 1
            while j < len(height):
                right_max = max(right_max, height[j])
                j += 1
            if min(left_max, right_max) - h >= 0:
                water += min(left_max, right_max) - h
        return water


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left_maxes = []
        tallest = 0
        for h in height:
            left_maxes.append(tallest)
            tallest = max(tallest, h)

        right_maxes = [0] * len(height)
        tallest = 0
        j = len(height) - 1
        while j >= 0:
            right_maxes[j] = tallest
            tallest = max(tallest, height[j])
            j -= 1

        for i,h in enumerate(height):
            if min(right_maxes[i], left_maxes[i]) - h >= 0:
                water += min(right_maxes[i], left_maxes[i]) - h
        return water