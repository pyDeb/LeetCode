# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = self.create_number_from_list(l1)
        second = self.create_number_from_list(l2)
        return self.number_to_reversed_list(first + second)
        
        
        
    
    #ln = list of numbers
    def create_number_from_list(self, head):
        number = ""
        
        temp = head
        while temp:
            number = str(temp.val) + number
            temp = temp.next
        
        return int(number)
        
        
    
    def number_to_reversed_list(self, number):
        number_str = str(number)
        result_list = ListNode()
        result_list.val = int(number_str[len(number_str) - 1])
        current = result_list
        for i in range(len(number_str) - 2, -1, -1):
            temp = ListNode()
            temp.val = int(number_str[i])
            current.next = temp
            current = current.next
        
        return result_list
            
