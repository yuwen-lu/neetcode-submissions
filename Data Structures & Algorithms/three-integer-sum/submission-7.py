class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if -(nums[i] + nums[j]) in nums[j+1:]:
                    tmp_result = sorted([nums[i], nums[j], -(nums[i] + nums[j])])
                    if tmp_result not in results:
                        results.append(tmp_result)
        return results