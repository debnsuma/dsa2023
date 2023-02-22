class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def zipper_lists(head_1, head_2):
  
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
            


    


    
            
            
            
    
