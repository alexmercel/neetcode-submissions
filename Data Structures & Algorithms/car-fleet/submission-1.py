class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l=[]
        for i in range(len(position)):
            l.append([position[i],speed[i]])
        l.sort(key=lambda x:x[0] ,reverse=True)
        print(l)
    
        time=[(target-l[0][0])/l[0][1]]
        for i in range(1,len(l)):
            t=(target-l[i][0])/l[i][1]
            time.append(max(t,time[-1]))
        return(len(set(time)))

    