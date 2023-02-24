class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, head_1, head_2):
        
        dummy_head = ListNode("Filler")
        tail = dummy_head
        
        while head_1 and head_2:
            
            if head_1.val < head_2.val:
                tail.next = head_1
                head_1 = head_1.next 
            else:
                tail.next = head_2
                head_2 = head_2.next 
                
            tail = tail.next 
        
        tail.next = head_1 or head_2
        
        return dummy_head.next 