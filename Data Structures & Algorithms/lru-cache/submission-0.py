
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} #map key -> nodes
        self.capacity = capacity

        #Left = LRU, Right = Most Recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next #get prev/next of node
        prev.next, nxt.prev = nxt, prev #set them to eachother, skipping node!

    #insert at RIGHT
    def insert(self, node):
        prev, nxt = self.right.prev, self.right #insert between right-1 and right
        prev.next = nxt.prev = node
        #reassign node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        #get most recent
        if key in self.cache:
            #update to most recent
            self.remove(self.cache[key]) #dedupe
            self.insert(self.cache[key]) #move to most recent

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        #add it 
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        #if overflow, remove
        if len(self.cache) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]