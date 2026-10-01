from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left =0
        dictionary = defaultdict(int)
        res=0
        maxf=0
        for right in range(len(s)):
            dictionary[s[right]] +=1
            maxf=max(maxf,dictionary[s[right]])
            if right - left - max(dictionary.values())+1 > k:
                dictionary[s[left]] -=1
                left +=1
            res = max(res, right-left+1)
        return res
            