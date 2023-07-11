# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def removeNth(point):
            if point is None:
                return (point,1)
            
            temp,idx = removeNth(point.next)
            if idx == n:
                return (temp,idx+1)
            else:
                point.next = temp
                return (point,idx+1)
        (head,idx) = removeNth(head)
        return head
