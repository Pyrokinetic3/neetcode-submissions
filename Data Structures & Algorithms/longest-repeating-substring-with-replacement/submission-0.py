class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker = {}
        longest = 0
        left = 0
        for i, let in enumerate(s):
            if let not in tracker:
                tracker[let] = 1
            else:
                tracker[let] += 1
            while i - left + 1 - max(tracker.values()) > k:
                tracker[s[left]] -= 1
                left += 1
            substring_length = i - left + 1
            longest = max(longest, substring_length)
        return longest