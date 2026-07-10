# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()            # throwaway placeholder; its .next becomes the real head
        curr = dummy                  # curr is always the tail of the list we're building
        while list1 and list2:        # only compare while BOTH have nodes
            if list1.val <= list2.val:
                curr.next = list1     # link the smaller node on
                list1 = list1.next    # advance that list
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next          # advance the tail (runs either way)

        curr.next = list1 or list2    # attach whatever's left; one is already None
        return dummy.next             # skip the placeholder, hand back the real head
