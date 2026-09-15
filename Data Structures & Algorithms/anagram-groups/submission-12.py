from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1=defaultdict(list)
        for s in strs:
            groups=[0]*26
            for j in s:
                groups[ord(j)-97] += 1
            dict1[tuple(groups)].append(s)
        return list(dict1.values())