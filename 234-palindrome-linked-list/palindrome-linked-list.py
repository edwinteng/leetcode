# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle
        fast,slow = head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        #slow is the middle of link list
        #reverse link list
        headhalf = slow
        dummy = ListNode()
        cur = headhalf
        while cur:
            tmp = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = tmp
        #traverse list 
        firstcur = head
        secondcur = dummy.next
        while secondcur:
            if firstcur.val!=secondcur.val:
                return False
            firstcur = firstcur.next
            secondcur = secondcur.next
        return True