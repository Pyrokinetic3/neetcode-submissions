class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxh = 0
        i = 0
        j = len(heights) - 1
        while j > i:
            temp_max = (j - i) * min(heights[j], heights[i])
            if temp_max > maxh:
                maxh = temp_max
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
        return maxh