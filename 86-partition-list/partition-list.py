# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #dummy = ListNode()
        #dummy.next = head
        cur = head

        dummy_bef = ListNode()
        cur_bef = dummy_bef
        dummy_aft = ListNode()
        cur_aft = dummy_aft
        while cur:
            if cur.val>=x:
                cur_aft.next = cur
                cur_aft =cur_aft.next
            else:
                cur_bef.next = cur
                cur_bef=cur_bef.next
            cur=cur.next
        cur_bef.next = dummy_aft.next
        cur_aft.next = None
        return dummy_bef.next

            