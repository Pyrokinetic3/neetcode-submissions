class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(list(set(nums))) != len(nums)