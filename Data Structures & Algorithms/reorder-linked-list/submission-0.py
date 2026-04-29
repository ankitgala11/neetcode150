# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow.next
        slow.next = None
        prev = None
        if not curr:
            return


        while curr:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
        
        rehead = head
        tail = rehead

        while tail:

            forward = tail.next
            forward2 = prev.next

            tail.next = prev
            prev.next = forward
            tail = forward
            prev = forward2
            if not prev:
                break



            
        