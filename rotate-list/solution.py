# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = ListNode()
        current = result
        length = 0
        modulo = 0
        
        # find the length of the list
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        
        if length > 0:
            modulo = k % length
        else:
            return None
        
        # Assigns the head of resutl
        result.val = self.return_value(head, (length - k) % length)
        
        for i in range(1, length):
            temp = ListNode()
            temp.val = self.return_value(head, ((length-k) + i) % length)
            current.next = temp
            current = current.next
        
        return result
        
        
    
    def return_value(self, head, index):
        current_ptr = head
        
        while(index):
            current_ptr = current_ptr.next
            index -= 1
        current_val = current_ptr.val
        return current_val
        
    
    
    
