class KthLargest:
    # create a min heap with only k largest numbers 
    # smallest value would be our Kth largest number
    
    # initialize list and use a for loop to call the add function on the numbers
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k 
        
        for i in nums:
            self.add(i)
        
        
    def add(self, val: int) -> int:
        # add the value to the heap and then heapify up
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)


        # limit the heap to k elements 
        if len(self.heap) > self.k:
            self.extract_min()

        # we have to return the kth largest , which is the root node cause its a min heap 
        return self.heap[0]
        

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1)//2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index] , self.heap[parent_index]

                index = parent_index 

            else:
                break 

    def extract_min(self):
        # swap root with last element and remove last element 
        self.heap[0] = self.heap.pop()
        # restore min heap property starting from new root 
        self.heapify_down(0)

    
    def heapify_down(self, index):
        
        length = len(self.heap)
        
        while True:
            left = 2*index + 1
            right = 2*index + 2
            smallest = index 

            if left < length and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < length and self.heap[right] < self.heap[smallest]:
                smallest = right 

            if smallest != index:
                self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
                index = smallest

            else:
                break 