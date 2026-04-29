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
          
            mp[tail] = new
            copytail.next = new
            copytail = copytail.next
            tail = tail.next

        copyhead= copyhead.next

        tail = head
        copytail = copyhead
        while tail:
            if tail.random is not None:
                copytail.random = mp[tail.random]

            tail = tail.next
            copytail = copytail.next

    
        return copyhead


        
            