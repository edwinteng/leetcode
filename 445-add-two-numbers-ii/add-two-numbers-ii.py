# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1,st2 = [],[]
        ptr1,ptr2 = l1,l2
        dummy = ListNode()
        while ptr1:
            st1.append(ptr1.val)
            ptr1=ptr1.next
        while ptr2:
            st2.append(ptr2.val)
            ptr2=ptr2.next
        carry,total = 0,0
        while st1 or st2 or carry:
            total=carry
            if st1:
                total+=st1.pop()
            if st2:
                total+=st2.pop()
            carry,digit = divmod(total,10)
            cur = ListNode(digit,dummy.next)
            dummy.next = cur
        return dummy.next