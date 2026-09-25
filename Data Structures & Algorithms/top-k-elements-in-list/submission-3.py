class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = []
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        while k > 0:
            best_num = max(count, key=count.get)
            output.append(best_num)
            del count[best_num]
            k -= 1
        return output