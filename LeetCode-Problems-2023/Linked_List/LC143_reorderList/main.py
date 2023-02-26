class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    
    def reorderList(self, head):
        
        # Handling the empty LL 
        if not head:
            return None
        
        # Find the middle of the LL
        middle = self.middleNode(head)
        
        # Reverse the second part of the LL 
        second_ll_head = self.reverseList(middle.next)
        middle.next = None 
        
        # Merge two LL 
        new_head = self.zipper_lists(head, second_ll_head)
        
        return new_head

    def middleNode(self, head):
        
        slow = head
        fast = head 
        
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next 
        return slow
    
    def reverseList(self, head):
        
        previous = None 
        current = head
        
        
        while current is not None:
            next = current.next 
            current.next = previous
            previous, current = current, next
            
        return previous 
    
    def zipper_lists(self, head_1, head_2):
    
        tail = head_1
        current1 = head_1.next
        current2 = head_2
        counter = 0
        
        while current1 is not None and current2 is not None:
            
            if counter % 2 == 0:
                tail.next = current2
                current2 = current2.next 
            else: 
                tail.next = current1
                current1 = current1.next 
            
            counter += 1
            tail = tail.next 
            
        if current1 is not None:
            tail.next = current1
        if current2 is not None:
            tail.next = current2
                    
        return head_1