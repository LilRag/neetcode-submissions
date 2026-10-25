# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # min heap 
        # insert the head node of each of the k lists into min heap 
        # pop the smallest node from the heap and append it to your merged list 
        # if that popped node has a next push the next into the heap 
        # repeat until heap is empty


        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i , node))

        dummy = ListNode(0)
        curr = dummy 

        while heap:
            val, i , node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next 

            if node.next:
                heapq.heappush(heap, (node.next.val, i , node.next))

        return dummy.next
