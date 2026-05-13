class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        result = 1
        for i in range(n-1):
            result = one + two
            two = one
            one = result
        return result