class Node:
    def __init__(self, key, val):
        self.key , self.val = key , val 
        self.prev = self.next = None 

class LRUCache:
    # all operations to be O(1) while following LRU
    # find a node by its key in O(1)
    # quickly move nodes to the most recently used position and remove least recently used node from other end in O(1)
    # most recently used to right side
    # least recently used to left side

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} # map key to node 

        self.left, self.right = Node(0,0) , Node(0,0)
        self.left.next, self.right.prev = self.right , self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt , prev

    def insert(self, node):
        prev,nxt = self.right.prev , self.right 
        prev.next = nxt.prev = node 
        node.next, node.prev = nxt, prev 


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return - 1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
