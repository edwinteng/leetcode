# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        ptr1,ptr2 = l1,l2
        while ptr1 or ptr2 or carry:
            total = carry
            if ptr1:
                total+=ptr1.val
                ptr1=ptr1.next
            if ptr2:
                total+=ptr2.val
                ptr2=ptr2.next
            carry,remainder=divmod(total,10)
            cur.next = ListNode(remainder)
            cur = cur.next     
        return dummy.next

        