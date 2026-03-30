class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s= "".join(i for i in s.split(" "))

        validchar=list("qazxswedcvfrtgbnhyujmkiolp1234567890")
        newstring=""
        for i in s:
            if i in validchar:
                newstring += i
        if newstring == newstring[::-1]:
            return True
        else:
            return False