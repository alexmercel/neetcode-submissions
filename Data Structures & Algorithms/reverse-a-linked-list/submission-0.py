# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 --> 2 --> 3
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        prev,curr= None,head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

        """
        if not head:
            return None
        if head.next == None:
            return head
        curr = head.next
        head.next = None
        while curr:
            temp = curr.next
            curr.next = head
            head = curr
            curr = temp
            
        return head


        