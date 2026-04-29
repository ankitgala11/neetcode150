# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        def rev(head):
            if not head:
                return

            curr = head
            prev = None
            cnt = 0

            tail = curr
            cntcheck = 0

            while tail and cntcheck<k:
                tail=tail.next
                cntcheck += 1
            
            if not tail and cntcheck != k:
                return curr
                

            while curr and cnt<k:
                forward = curr.next
                curr.next = prev
                prev = curr
                curr = forward
                cnt += 1
            

            

            head.next = rev(curr)
            return prev

        return rev(head)