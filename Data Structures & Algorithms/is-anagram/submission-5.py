class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        a=len(s)
        if a != len(t):
            return False
        for i in range (a):
            dict1[s[i]] = dict1.get(s[i],0) + 1
            dict1[t[i]] = dict1.get(t[i],0) - 1
        if set(dict1.values()) == {0}:
            return True
        return False

        