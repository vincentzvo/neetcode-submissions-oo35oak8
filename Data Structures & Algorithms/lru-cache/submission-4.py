class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        next = prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.l = self.r = Node(0, 0)
        self.l.next = self.r
        self.r.prev = self.l
    
    def remove(self, node):
        nxt = node.next
        prev = node.prev
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        nxt = self.r
        prev = self.r.prev
        node.next = nxt
        node.prev = prev
        nxt.prev = prev.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lRU = self.l.next
            self.remove(lRU)
            del self.cache[lRU.key]
        
