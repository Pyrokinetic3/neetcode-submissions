class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                    if nums[i] + nums[j] == target and i != j:
                        output = [min(i,j), max(i,j)]
                        return output

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}
        for i, num in enumerate(nums):
            counts[num] = i
        for i, k in enumerate(nums):
            result = target - k
            if result in counts and counts[result] != i:
                output = [min(counts[result], i), max(counts[result], i)]
                return output