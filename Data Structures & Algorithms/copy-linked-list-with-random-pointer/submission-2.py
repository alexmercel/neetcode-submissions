"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        oldtonew={None:None}

        current = head
        while current:
            oldtonew[current] = Node(current.val)
            current = current.next
        
        current = head

        while current:
            copy= oldtonew[current]
            copy.next=oldtonew[current.next]
            copy.random=oldtonew[current.random]
            current = current.next
        return oldtonew[head]