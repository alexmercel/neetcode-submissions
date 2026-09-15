class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for i in range (len(strs)):
            dict1["".join(sorted(strs[i]))] = dict1.get("".join(sorted(strs[i])),[]) + [strs[i]]
        return list(dict1.values())