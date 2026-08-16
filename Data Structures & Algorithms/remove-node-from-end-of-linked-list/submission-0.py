# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None 

        # fast-slow trick 
        # make fast pointer n nodes ahead of slow, when fast terminates, slow is at the correct position , then delete 


        # dummy node to delete the head itself
        dummy = ListNode(0, head)

        slow = dummy 
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # it would loop until fast hits the end 
        # slow is sitting right before the node we want to delete 
        slow.next = slow.next.next

        # return actual head 
        return dummy.next 
