# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False 

        temp = head        
        visited = set()

    
        while temp.next != None:
            if temp in visited:
                return True
            visited.add(temp) 
            temp = temp.next 

        return False