# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptra = headA
        ptrb = headB
        #while ptra or ptrb:
        while ptra != ptrb:
            #if ptra and ptrb and ptra.val == ptrb.val:
            #    return ptra.val
            #if ptra is None:
            #    ptra = headB
            #else:
            #    ptra = ptra.next
            #if ptrb is None:
            #    ptrb = headA
            #else:
            #    ptrb = ptrb.next
            #ptra = ptra.next
            #ptrb = ptrb.next
            ptra = ptra.next if ptra else headB
            ptrb = ptrb.next if ptrb else headA
        return ptra