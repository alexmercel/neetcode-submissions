class Solution:

    def encode(self, strs: List[str]) -> str:
        data=""
        for i in strs:
            data = data + str(len(i)) + "#" + i
        return data

    def decode(self, s: str) -> List[str]:

        res=[]
        i = 0
        while i < len(s):
            # Find the delimiter starting from current index i
            j = s.find('#', i)
            
            # Extract length and the string itself
            length = int(s[i:j])
            content = s[j + 1 : j + 1 + length]
            res.append(content)
            
            # Move pointer to the start of the next segment
            i = j + 1 + length
        return res

