class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        if s_nums[0] > 0:
            return []
        results = []
        
        for i, n in enumerate(s_nums):
            left = i+1
            right = len(s_nums) - 1
            while left < right:
                if s_nums[left] + s_nums[right] + s_nums[i] == 0:
                    if [s_nums[left], s_nums[right], s_nums[i]] not in results:
                        results.append([s_nums[left], s_nums[right], s_nums[i]])
                    while left < right and s_nums[left] == s_nums[left + 1]:
                        left += 1
                    while left < right and s_nums[right] == s_nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s_nums[left] + s_nums[right] + s_nums[i] > 0:
                    right -= 1
                else:
                    left += 1
        return results