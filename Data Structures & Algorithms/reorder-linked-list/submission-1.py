# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):

        prev , curr = None  , head 
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the list into two 
        # reverse the second list 
        # merge, 
        # [0, n-1. 1 , n-2, 3, n-3 ..]
        if head is None:
            return None 
        
        slow, fast = head, head 

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next 

            
        after_slow = slow.next
        slow.next = None  
        reversed_list = self.reverseList(after_slow)
        
        p1 = head
        p2 = reversed_list 
        
        while p2:
            temp1 = p1.next
            temp2 = p2.next

            p1.next = p2 
            p2.next = temp1
            
            p1 = temp1 
            p2 = temp2 
