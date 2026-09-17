class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i,num in enumerate(nums):
            temp = nums.copy()
            del temp[i]
            value = 1
            for k in temp:
                value *= k
            output.append(value)
        return output

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left_product = 1
        for num in nums:
            output.append(left_product)
            left_product *= num
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        return output