# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        fast = dummy 
        slow = dummy 


        for _ in range(n):
            fast = fast.next 

        while fast.next != None:
            slow = slow.next 
            fast = fast.next 

            # when fast reaches the end , slow is sitting right before the nth node 

        slow.next = slow.next.next 

        return dummy.next  