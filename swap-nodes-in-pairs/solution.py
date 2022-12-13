# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        current_node = head
        next_node = current_node.next
        current_node.next = current_node.next.next
        next_node.next = current_node
        head = next_node
        current_node = head.next

        while current_node.next is not None and current_node.next.next is not None:
            next_node = current_node.next
            next_next_node = next_node.next
            
            next_node.next = next_next_node.next
            current_node.next = next_next_node
            next_next_node.next = next_node

            current_node = next_node
        
        return head
            
