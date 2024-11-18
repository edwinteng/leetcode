# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        #dummy = ListNode()
        
        #if cur is None or cur.next is None:
        #    return head

        while cur and cur.next:
            # if the same, remove next
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur=cur.next
        
        return head