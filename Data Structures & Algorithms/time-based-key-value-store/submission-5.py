from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp,value])
        return

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashmap:
            lis = self.hashmap[key]
            l=0
            r=len(lis)
            while l<r:
                mid=(l+r)//2
                # print(mid,lis,lis[mid],timestamp)
                if lis[mid][0] > timestamp:
                    r = mid
                else:
                    l= mid+1
            if l-1<0:
                return ""
            return lis[l-1][1]
        else:
            return ""
        