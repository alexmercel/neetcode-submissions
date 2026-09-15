from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1=defaultdict(list)
        for i in range (len(strs)):
            groups=[0]*26
            for j in strs[i]:
                groups[ord(j)-97] += 1
            dict1[tuple(groups)] += [strs[i]]
        return list(dict1.values())