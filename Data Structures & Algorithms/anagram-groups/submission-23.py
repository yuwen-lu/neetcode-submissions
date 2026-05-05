class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            if "".join(sorted(s)) in result:
                result["".join(sorted(s))].append(s)
            else:
                result["".join(sorted(s))] = [s]
        return list(result.values())
