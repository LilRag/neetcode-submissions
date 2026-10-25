# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast and slow pointer to find mid 
        # sever list into two independent halves 

        # conquer 
        # recursively sort left and right half 

        # merge
        # use dummy head to weave sorted list 

        if not head or not head.next:
            return head 

        mid = self.get_mid_split(head)

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)


    def get_mid_split(self, head):

        prev = None 
        slow = fast = head

        while fast and fast.next:
            prev = slow 
            slow = slow.next
            fast = fast.next.next 
        # prev is before the mid 
        # slow is at the mid 
        # fast is in the end 
        # disconnect the left half from the right half 
        if prev:
            prev.next = None 

        return slow # head of the right half 


    def merge(self, l1, l2 ):
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

