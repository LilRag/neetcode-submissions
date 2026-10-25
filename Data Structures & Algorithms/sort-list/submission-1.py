# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # basecase
        if not head or not head.next:
            return head 

        mid = self.get_split(head)

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)


    def get_split(self, head):
        
        prev = None
        slow = head
        fast = head 

        while fast and fast.next:
            prev = slow 
            slow = slow.next
            fast = fast.next.next 

        if prev:
            # sever tje link
            prev.next = None 

        return slow 

    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next

            else:
                curr.next = l2 
                l2 = l2.next
            curr = curr.next  

        curr.next = l1 or l2 
            
        return dummy.next 
