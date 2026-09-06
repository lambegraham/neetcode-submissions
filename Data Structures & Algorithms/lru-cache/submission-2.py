class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} #key -> value
        self.capacity = capacity

        #init pointers
        #LRU = Left, MRU = right
        self.left, self.right = Node(0,0), Node(0,0) #dummy nodes
        self.left.next, self.right.prev = self.right, self.left #set directions
    def remove(self, node):
        #remove the node completely, do this by reassinging node.prev/next to eachother
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        #insert into the end of our LRU
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) #remove it
            self.insert(self.cache[key]) #insert at end (most recently used)
            return self.cache[key].val #return the value of key
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        #if len exceeds it, remove
        if len(self.cache) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
