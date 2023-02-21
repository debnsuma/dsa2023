'''
Problem : https://structy.net/problems/get-node-value
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 
        
def get_node_value(head, index):
    
    current_pointer = 0 
    
    while head is not None:
        
        if current_pointer == index:
            return head.val 
        
        head = head.next 
        current_pointer += 1
        
    else:
        return None