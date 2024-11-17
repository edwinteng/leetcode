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
        while l1 or l2 or carry:
            sum_tmp = carry
            if l1:
                sum_tmp+=l1.val
                l1=l1.next
            if l2:
                sum_tmp+=l2.val
                l2=l2.next
            carry,cur_sum = divmod(sum_tmp,10)
            cur.next = ListNode(cur_sum)
            cur = cur.next

        return dummy.next

        