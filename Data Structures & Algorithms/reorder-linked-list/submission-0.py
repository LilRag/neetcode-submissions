# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the list into two 
        # reverse the second list
        # merge 
        if head is None:
            return None

        # find the split 
        fast, slow = head, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next 


        # reverse 2nd list 
        curr = slow.next 
        slow.next = None # sever the first half from the second 
        prev = None 

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #list1 is start of first list , prev is start of second list 
        list1 = head 
        list2 = prev 
        
        while list2:
            #save next nodes before we override the pointers
            temp1 = list1.next
            temp2 = list2.next 

            list1.next = list2
            list2.next = temp1 

            list1 = temp1
            list2 = temp2 

              
