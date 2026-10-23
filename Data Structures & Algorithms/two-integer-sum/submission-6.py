class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for i in range(len(nums)):
            tracker[nums[i]] = i
        for j in range(len(nums)):
            n = target - nums[j]
            if n in tracker and tracker[n] != j:
                return [min(tracker[n], j), max(tracker[n], j)]