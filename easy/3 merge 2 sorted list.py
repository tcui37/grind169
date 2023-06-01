# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sorted_list = ListNode(0)
        dummy = sorted_list

        while list1 and list2:
            if list1.val < list2.val:
                sorted_list.next = ListNode(list1.val)
                sorted_list = sorted_list.next
                list1 = list1.next
            else:
                print(list1.val, list2.val)
                sorted_list.next = ListNode(list2.val)
                sorted_list = sorted_list.next
                list2 = list2.next
        if list1:
            sorted_list.next = list1
        if list2:
            sorted_list.next = list2
        return dummy.next
