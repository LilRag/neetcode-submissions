"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)

        curr_original = head
        curr_new = dummy
        hashmap = {None:None}

        while curr_original:
            new_node = Node(curr_original.val)
            hashmap[curr_original] = new_node


            curr_new.next = new_node 

            curr_new = curr_new.next 
            curr_original = curr_original.next

        curr_original = head
        temp = dummy.next 

        while curr_original:

            temp.next = hashmap[curr_original.next]
            temp.random = hashmap[curr_original.random]

            temp = temp.next 
            curr_original = curr_original.next

        return dummy.next