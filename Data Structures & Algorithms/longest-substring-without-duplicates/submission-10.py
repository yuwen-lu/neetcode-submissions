class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest_s = s[0]
        lr = 1
        i = 0
        j = 1
        while j < len(s):
            if s[j] in longest_s:
                idx = longest_s.index(s[j])
                i = i + idx + 1
            j += 1
            longest_s = s[i:j]
            lr = max(lr, len(longest_s))
        return lr