# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = head
        cnt = 0
        curr= head
        while curr:
            curr=curr.next
            cnt += 1

        if n==cnt:
            return head.next

        for i in range(n):
            fast = fast.next

        
        slow=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next

        
        slow.next=slow.next.next

        return head


