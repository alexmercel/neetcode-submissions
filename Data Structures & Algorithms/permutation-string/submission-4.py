class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        b=list(s1)
        b.sort()
        for i in range (len(s2)-len(s1)+1):
            a= list(s2[i:i+len(s1)])
            a.sort()
            if a==b:
                return True

        return False
        