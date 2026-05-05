import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        for idx, num in enumerate(nums):
            new_list = [val for i, val in enumerate(nums) if i != idx]
            output[idx] = math.prod(new_list)
        return output