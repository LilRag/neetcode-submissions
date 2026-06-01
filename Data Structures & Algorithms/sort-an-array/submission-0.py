class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def heapify(arr, n , i ):

            largest = i 
            l = 2*i + 1
            r = 2*i + 2 

            if l < n and arr[l] > arr[largest]:
                largest = l 

            if r< n and arr[r] > arr[largest]:
                largest = r

            if largest != i :
                arr[i], arr[largest] = arr[largest] , arr[i]

                heapify(arr, n , largest)

        def heapsort(arr):
            n = len(arr)
            # building the heap 
            # consider all the parent nodes 
            for i in range(n//2 -1 , -1 , -1 ):
                heapify(arr, n , i )

            # extract an element from the heap one by one 
            for i in range(n-1 , 0 , -1):
                # move current root to the end and not counting it for further heapify 
                arr[0], arr[i] = arr[i] , arr[0]
                # call heapify on reduced heap 
                heapify(arr, i , 0 )


        heapsort(nums)
        return nums 