# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        minh = []

        j=0
        for i in lists:
            heapq.heappush(minh, (i.val,j, i))
            j+=1

        dummy = ListNode(0)
        tail = dummy

        while minh:
            key ,j, node = heapq.heappop(minh)
            if node.next:
                heapq.heappush(minh, (node.next.val,j, node.next))

            tail.next = node
            tail = tail.next

        
        return dummy.next


