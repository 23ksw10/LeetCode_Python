# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=None
        h=head
        while h:
            tmp=h
            h=h.next
            tmp.next=t
            t=tmp
        return t
