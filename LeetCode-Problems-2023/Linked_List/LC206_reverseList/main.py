class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    
    def reverseList(self, head):
        
        previous = None 
        current = head
        
        
        while current is not None:
            next = current.next 
            current.next = previous
            previous, current = current, next
            
            print(previous.val)

        return previous 