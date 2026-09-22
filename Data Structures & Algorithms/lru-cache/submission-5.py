class Node(object):
    def __init__ (self, key,val,prev=None,next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head,self.tail=Node(None,None,None,None),Node(None,None,None,None)
        self.head.next=self.tail
        self.tail.prev=self.head


    def get(self, key: int) -> int:
        if key in self.cache:
            #removed the node
            self.cache[key].next.prev=self.cache[key].prev
            self.cache[key].prev.next=self.cache[key].next
            #adding it to the end
            self.cache[key].next = self.tail
            self.cache[key].prev = self.tail.prev
            self.tail.prev.next = self.cache[key]
            self.tail.prev = self.cache[key]
            # print(self.cache)
            return self.cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.next.prev=node.prev
            node.prev.next=node.next
            del self.cache[key]

        elif len(self.cache)>=self.capacity:
            lru=self.head.next
            self.head.next=lru.next
            lru.next.prev=self.head
            del self.cache[lru.key]



        self.cache[key]=Node(key,value,self.tail.prev,self.tail)
        self.tail.prev.next=self.cache[key]
        self.tail.prev=self.cache[key]
        # print(self.cache)

            
        
