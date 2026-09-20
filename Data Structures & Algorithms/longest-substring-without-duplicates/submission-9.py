class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = {}
        left = 0
        count_max = 0

        for i, let in enumerate(s):
            if let in tracker and tracker[let] >= left:
                left = tracker[let] + 1

            tracker[let] = i
            count = i - left + 1
            count_max = max(count_max, count)

        return count_max