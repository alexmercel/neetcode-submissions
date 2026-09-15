class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for i in range (len(strs)):
            dict2=[0]*26
            for j in strs[i]:
                dict2[ord(j)-97] += 1
            dict1[str(dict2)] = dict1.get(str(dict2),[]) + [strs[i]]
        return list(dict1.values())