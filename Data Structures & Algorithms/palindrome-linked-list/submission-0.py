# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverselist(self, head):
        prev , curr = None , head 

        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 

        return prev 

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find mid 
        # reverse the second half 
        # compare 
        if not head or not head.next:
            return True 

        fast, slow = head, head 
        
        while fast.next and fast.next.next:
            fast = fast.next.next 
            slow = slow.next 

        
        # slow is at the mid point
        after_slow = slow.next
        reversed_list = self.reverselist(after_slow)

        p1 = head
        p2 = reversed_list
        is_pal = True 

        while p2:
            if p1.val != p2.val:
                is_pal = False
                break 
            p1 = p1.next
            p2 = p2.next 

       
        return is_pal 
