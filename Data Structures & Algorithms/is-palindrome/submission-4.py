class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [c.lower() for c in s if c.isalnum()]
        print(new_s)
        for idx, c in enumerate(new_s):
            if idx > len(new_s) / 2:
                return True
            else:
                if new_s[idx] != new_s[len(new_s) - idx - 1]:
                    return False
        return True
