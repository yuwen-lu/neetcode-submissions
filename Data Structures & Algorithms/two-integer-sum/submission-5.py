class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_nums:
                return [prev_nums[diff], i]
            prev_nums[num] = i
        return []
            