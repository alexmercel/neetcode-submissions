class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        a=dict()
        for i in range(len(strs)):
            m=str(sorted(strs[i]))
            if m in a.keys():
                a[m].append(i)
            else:
                a[m] = [i]
        print (a)
        for i in a:
            print (a[i],strs)
            b=[]
            for j in a[i]:
                b.append(strs[j])
            result.append(b)
        return result
        
