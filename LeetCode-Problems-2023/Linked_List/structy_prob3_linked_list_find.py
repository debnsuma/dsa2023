'''
Problem : https://structy.net/problems/linked-list-find
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None  

def linked_list_find(head, target):
    
    while head is not None:
        if head.val == target:
            return True
        
        head = head.next
    
    else:
        return False 
