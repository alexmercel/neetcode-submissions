class Solution:

    def encode(self, strs: List[str]) -> str:
        ret=""
        for i in strs:
            ret+=str(len(i))
            ret+="#"
            ret+=i
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        i=0
        ans=[]

        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i=j+1
            j=i+length
            ans.append(s[i:j])
            i = j
        return ans
