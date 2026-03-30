class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l=[]
        for i in range(len(position)):
            l.append([position[i],speed[i]])
        l.sort(key=lambda x:x[0] ,reverse=True)
        print(l)
    
        time=[]
        for i in l:
            time.append((target-i[0])/i[1])
        print(time)

        for i in range(1,len(time)):
            if time[i-1]>time[i]:
                time[i]=time[i-1]
        return (len(set(time)))


