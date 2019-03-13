from LinkedList import LinkedList as LL
from LinkedList import Node as Node

# Test cases
# Set up some Elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a LinkedList
ll = LL(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_from_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_from_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_from_position(1).value
# Should print 4 now
print ll.get_from_position(2).value
# Should print 3 now
print ll.get_from_position(3).value
