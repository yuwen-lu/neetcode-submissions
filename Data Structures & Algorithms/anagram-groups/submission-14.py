class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            flag = False
            for key in result.keys():
                if sorted(s) == sorted(key):
                    result[key].append(s)
                    flag = True
                    break
            if not flag:
                result[s] = [s]
        return list(result.values())
