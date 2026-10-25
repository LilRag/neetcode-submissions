# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverselinkedlist(self, head: Optional[ListNode])->Optional[ListNode]:
            prev, curr = None , head 
            while curr:
                temp = curr.next
                curr.next = prev 
                prev = curr
                curr = temp 

            return prev 


    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # reverse position of the list from left to right right integer 
        # so have a function that does reverse 
        # in the main function set the limits and call the function 

        if left == right or not head:
            return head  

        dummy = ListNode(0, head)
        # we have to reach before left 
        before_left = dummy 
        for _ in range(left - 1):
            before_left = before_left.next 

        # reach right node 
        right_node = before_left 
        for _ in range(right - left +1):
            right_node = right_node.next

        
        left_node = before_left.next
        after_right = right_node.next

        #sever the connections 
        before_left.next = None
        right_node.next = None 

        new_sub_head = self.reverselinkedlist(left_node)

        before_left.next = new_sub_head
        left_node.next = after_right # connect old sublist head (the tail now)

        return dummy.next




         
