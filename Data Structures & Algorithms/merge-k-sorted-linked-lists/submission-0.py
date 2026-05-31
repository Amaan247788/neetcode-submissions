# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        def mergeTwoLists(list1: ListNode, list2: ListNode) -> Optional[ListNode]:
            h1 = list1
            h2 = list2
            dummy = ListNode()
            curr = dummy

            while h1 and h2:
                if h1.val < h2.val:
                    curr.next = h1
                    h1 = h1.next
                else:
                    curr.next = h2
                    h2 = h2.next
                curr = curr.next
            if h1:
                curr.next = h1
            if h2:
                curr.next = h2
            return dummy.next

        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i - 1], lists[i])

        return lists[-1]

