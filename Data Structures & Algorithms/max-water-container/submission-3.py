class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_res = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            max_res = max(max_res, (j - i) * min(heights[i], heights[j]))
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return max_res