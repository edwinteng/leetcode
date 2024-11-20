# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
    def __init__(self,node):
        self.node = node
    def __lt__(self,other):
        return self.node.val < other.node.val
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        # cur.val  cur
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h,Node(lists[i]))
        dummy = ListNode()
        ptr = dummy
        while h:
            cur = heapq.heappop(h)
            ptr.next= cur.node
            ptr = ptr.next
            if cur.node.next:
                heapq.heappush(h,Node(cur.node.next))
        return dummy.next