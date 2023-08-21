# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = head, head
        # 1 - 2 - 3 - 4 - 5 - 6
        # 2, 3 | 3, 5 | 4 - 6
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        
        return p1

        
        
