class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        def insert(val):
            heap.append(val)
            heapify(len(heap)-1)

        def heapify(index):
            while index > 0:
                parent_index = (index - 1)//2
                if heap[parent_index] < heap[index]:
                    heap[parent_index] , heap[index] = heap[index], heap[parent_index]
                    index = parent_index    
                else:
                    break 

        def extract_max():
            if not heap:
                return None

            if len(heap) == 1:
                return heap.pop()

            max_val = heap[0]
            heap[0] = heap.pop()
            heapify_down(0)
            return max_val 

        def heapify_down(index):
            length = len(heap)

            while True:
                left_child_index = 2*index + 1 
                right_child_index = 2*index + 2
                largest = index 

                if left_child_index < length and heap[left_child_index] > heap[largest]:
                    largest = left_child_index

                if right_child_index < length and heap[right_child_index] > heap[largest]:
                    largest = right_child_index

                # if largest is not the current node, swap and continue 
                if largest != index:
                    heap[index] ,heap[largest] = heap[largest] ,heap[index]
                    index = largest
                else:
                    break

        for i in range(len(stones)):
            insert(stones[i])

        while len(heap) >1: 
            x = extract_max()
            y = extract_max()

            if x > y: 
                insert(x-y)
                 
        if len(heap) == 1:
            return heap[0]

        else:
            return 0

            
        
            
        

                 
