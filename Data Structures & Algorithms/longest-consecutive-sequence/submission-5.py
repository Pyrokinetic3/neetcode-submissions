class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        k = 0
        list1 = []
        if len(nums) == 0:
            return 0
        length = 1
        if nums:
            list1.append(nums[k])
            while k < len(nums) - 1:
                if nums[k] + 1 == nums[k+1]:
                    list1.append(nums[k+1])
                    if len(list1) > length:
                        length = len(list1)
                else:
                    list1 = []
                    list1.append(nums[k+1])
                k += 1
        return length