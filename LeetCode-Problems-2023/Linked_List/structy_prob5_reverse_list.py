'''
Problem : https://structy.net/problems/reverse-list
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 

def reverse_list(head):
    
    previous = None 
    current = head
    
    
    while current is not None:
        next = current.next 
        current.next = previous
        previous, current = current, next
        
        print(previous.val)

    return previous         

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

reverse_list(a)
        
        
