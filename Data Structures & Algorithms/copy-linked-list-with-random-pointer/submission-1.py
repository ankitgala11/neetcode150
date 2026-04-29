"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copyhead =copytail= Node(-1)
        tail = head
        mp = {}

        while tail:
            new =  Node(tail.val)
            copytail.next = new
            copytail = copytail.next
            tail = tail.next

        copyhead= copyhead.next

        curr = head
        copy = copyhead

        while curr:
            forward1 = curr.next
            curr.next = copy
            forward2 = copy.next
            copy.next = forward1
            curr= forward1
            copy = forward2
        
        curr = head
        

        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            
            curr= curr.next.next
        
        curr = head
        copy = copyhead

        while copy:
            curr.next = curr.next.next
            if copy.next:copy.next = copy.next.next

            curr = curr.next
            copy = copy.next
        
        return copyhead


        
            