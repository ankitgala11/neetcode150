# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # curr = head
        # prev = None


        # while curr:
        #     forward = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = forward
            
        # return prev

        def rev(head):
            if not head or not head.next:
                return head

            revh = rev(head.next)

            head.next.next = head
            head.next=None
            return revh

        return rev(head)