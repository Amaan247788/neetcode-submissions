# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        if not list1 and not list2:
            return None
        elif list1 and not list2:
            newHead = list1
            list1 = list1.next
        elif list2 and not list1:
            newHead = list2
            list2 = list2.next
        else:
            if list1.val <= list2.val:
                newHead = list1
                list1 = list1.next
            else:
                newHead = list2
                list2 = list2.next
        
        curr = newHead

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next

        while list1:
            curr.next = list1
            curr = curr.next
            list1 = list1.next

        while list2:
            curr.next = list2
            curr = curr.next
            list2 = list2.next
        
        return newHead
        
