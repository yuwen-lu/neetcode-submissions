class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_res = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                max_res = max((j - i) * min(heights[i], heights[j]), max_res)
        return max_res