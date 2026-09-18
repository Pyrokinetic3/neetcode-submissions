class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        count = {}
        for i,num in enumerate(numbers):
            needed = target - num
            if needed in count:
                return [min([count[needed]+1, i+1]), max([count[needed]+1, i+1])]
            count[num] = i