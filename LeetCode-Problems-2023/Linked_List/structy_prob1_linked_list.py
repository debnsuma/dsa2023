'''
Problem : https://structy.net/problems/linked-list-values
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None    
        
def linked_list_values(head):
    
    result = []
    
    while head is not None:
        result.append(head.val)
        head = head.next
    
    print(result)
    return result 



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_values(a) # -> [ 'a', 'b', 'c', 'd' ]