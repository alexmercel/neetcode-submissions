class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        a=dict()
        for i in range(len(strs)):
            m=str(sorted(strs[i]))
            if m in a.keys():
                a[m].append(strs[i])
            else:
                a[m] = [strs[i]]
        for i in a:
            result.append(a[i])
        return result
        
