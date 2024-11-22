# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        fast = head
        slow = dummy
        while fast:
            while fast and fast.next and fast.val == fast.next.val:
                fast = fast.next
            # if slow.next is fast, it means there is only one element with fast
            if slow.next != fast:
                slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
        return dummy.next