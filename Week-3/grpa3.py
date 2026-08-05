#given a linked list we have to reverse it 

def reverse(root):
    prev = None
    current = root
    while current is not None:
        nextnode = current.next # save the next node . so while pointing first node to the node we does'n loose the pointer that point the other nodes
        current.next = prev # Simply it is used to reverse the arrow . It points the first node to the none
        prev = current # Move previous
        current = nextnode # Move current 
    return prev