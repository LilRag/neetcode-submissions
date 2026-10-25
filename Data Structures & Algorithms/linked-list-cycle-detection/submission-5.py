# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # one fast pointer, moving twice as fast 
        # one slow pointer
        # if fast and slow pointer are the same at any point , there might be a cycle 

        if not head:
            return False

        slow, fast = head, head 
        
        while fast != None and fast.next != None:
            fast = fast.next.next 
            slow = slow.next 

            if fast == slow:
                return True 

        return False