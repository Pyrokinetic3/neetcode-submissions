class SolutionBrute:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        i = 0
        while i < len(nums)-2:
            k = i + 1
            while k < len(nums)-1:
                j = k + 1
                while j < len(nums):
                    temp = sorted([nums[i],nums[k],nums[j]])
                    if nums[i] + nums[k] + nums[j] == 0 and temp not in output:
                        output.append(temp)
                    j += 1
                k += 1
            i += 1
        return output

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    output.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return output
            