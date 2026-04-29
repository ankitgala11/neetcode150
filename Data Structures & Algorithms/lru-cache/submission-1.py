class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp={}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)

        self.head.next=self.tail
        self.tail.prev = self.head


    def insertAfterHead(self, node):

        node.next = self.head.next
        node.prev = self.head

        node.next.prev = node
        self.head.next = node

    def delete(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev
        
    def get(self, key: int) -> int:
        if key in self.mp:
            node = self.mp[key]

            self.delete(node)
            self.insertAfterHead(node)

            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.mp:
            node = self.mp[key]
            self.delete(node)
            self.insertAfterHead(node)
            node.val = value
        
        else:
            node = Node(key, value)
            if len(self.mp)<self.capacity:
                self.insertAfterHead(node)
                self.mp[key] = node
            else:
                nodetodelete = self.tail.prev
                del self.mp[nodetodelete.key]
                self.delete(nodetodelete)
                self.insertAfterHead(node)
                self.mp[key] = node



        
