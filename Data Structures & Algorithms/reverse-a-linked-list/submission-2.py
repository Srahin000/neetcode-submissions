# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, hd: Optional[ListNode]) -> Optional[ListNode]:
        prev = None


        while hd:
            temp = hd.next
            hd.next = prev
            prev = hd
            hd = temp
        return prev 
        