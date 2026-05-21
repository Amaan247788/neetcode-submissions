# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        dummy = head

        ans = ListNode()
        ans = head

        head = head.next

        dq = deque()

        while head:
            dq.append(head)
            head = head.next

        right = True
        while dq:
            if right:
                dummy.next = dq[-1]
                dq.pop()
                dummy = dummy.next
            else:
                dummy.next = dq[0]
                dq.popleft()
                dummy = dummy.next
            right = not right
        
        if dummy:
            dummy.next = None

        return