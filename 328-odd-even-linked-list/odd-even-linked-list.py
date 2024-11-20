# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = 1
        cur = head

        dummy_odd = ListNode()
        cur_odd = dummy_odd
        dummy_even = ListNode()
        cur_even = dummy_even
        while cur:
            if index %2 ==1:
                cur_odd.next = cur
                cur_odd=cur_odd.next
            else:
                cur_even.next = cur
                cur_even = cur_even.next
            index+=1
            cur=cur.next
        cur_odd.next=dummy_even.next
        cur_even.next= None
        return dummy_odd.next