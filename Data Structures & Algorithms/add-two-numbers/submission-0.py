# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def rev(head):

            curr= head
            prev = None

            while curr:
                forward = curr.next
                curr.next = prev
                prev = curr
                curr=forward


            return prev

        
        curr1= l1
        curr2 = l2

        carry = 0
        dummy =tail = ListNode(-1)

       
        while curr1 and curr2:
            temp = curr1.val + curr2.val + carry
            tail.next = ListNode(temp % 10)
            tail = tail.next
            carry = temp//10
            curr1=curr1.next
            curr2 = curr2.next

        while curr1:
            temp = curr1.val + carry
            tail.next = ListNode(temp % 10)
            tail = tail.next
            carry = temp//10
            curr1=curr1.next
            
        
        while curr2:
            temp =  curr2.val + carry
            tail.next = ListNode(temp % 10)
            tail = tail.next
            carry = temp//10
            curr2 = curr2.next

        while carry:
            temp = carry
            tail.next = ListNode(temp % 10)
            tail = tail.next
            carry = temp//10

        dummy = dummy.next

        return dummy
