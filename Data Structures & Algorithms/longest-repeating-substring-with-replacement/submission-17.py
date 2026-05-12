class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        result = 0

        # in the loop TODO define loop criteria
        while r < len(s):
            sub = s[l:r+1]

            freq = {}
            for i in sub:
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i] = 1
            sort_freq = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))
            if len(sub) - list(sort_freq.values())[0] <= k:
                r += 1
                if len(sub) > result:
                    result = len(sub)
            else:
                l += 1
                if r < l:
                    r = l
    
        return result

