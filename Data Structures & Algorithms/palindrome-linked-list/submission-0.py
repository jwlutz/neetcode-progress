# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        curr = head
        while curr:
            array.append(curr.val)
            curr = curr.next
        return array == array[::-1]