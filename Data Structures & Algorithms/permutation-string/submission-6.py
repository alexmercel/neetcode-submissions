from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def checkperm(s1,s2):
            hashmap=defaultdict(int)
            for i in range(len(s1)):
                hashmap[s1[i]]+=1
                hashmap[s2[i]]-=1
            if list(hashmap.values()) == [0]*len(hashmap.values()):
                return True
            return False
        if len(s2)<len(s1):
            return False
        else:
            for i in range(0,len(s2)-len(s1)+1):
                # print ((s1,s2[i:i+len(s1)]))
                if checkperm(s1,s2[i:i+len(s1)]):
                    return True
            return False

            
