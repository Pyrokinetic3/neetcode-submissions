class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, remaining - nums[i])
                path.pop()

        backtrack(0, [], target)
        return result