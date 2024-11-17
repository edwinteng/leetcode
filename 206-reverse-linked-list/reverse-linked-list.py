# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = head
        while ptr:
            #step 1: save the next node in the list
            tmp = ptr.next

            #connect the current node and the new list
            #point current node's next to dummy's pointer
            #point dummy to the current node
            ptr.next = dummy.next
            dummy.next = ptr

            #step 2: keep going
            ptr = tmp
        return dummy.next