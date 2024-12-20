from typing import List

class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

    def twoSumSorted(self, nums: List[int], target: int) -> List[int]:
        sorted_nums  = sorted(enumerate(nums), key=lambda x: x[1])
        left = 0
        right = len(nums) - 1
        while left < right:
            current_sum = sorted_nums[left][1] + sorted_nums[right][1]
            if current_sum == target:
                return sorted_nums [left][0], sorted_nums [right][0]
            if current_sum > target:
                right -= 1
            if current_sum < target:
                left = left + 1

    def twoSumBest(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return hash_map[complement], i
            hash_map[nums[i]] = i


nums = [2,1,6,3,5,4]
target = 11
s = Solution()
print(s.twoSumBruteForce(nums, target))
print(s.twoSumSorted(nums, target))
print(s.twoSumBest(nums, target))