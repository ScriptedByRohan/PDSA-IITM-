#given a linked list we have to reverse it 

def reverse(root):
    prev = None
    current = root
    while current is not None:
        nextnode = current.next
        current.next = prev
        prev = current
        current = nextnode
    return prev