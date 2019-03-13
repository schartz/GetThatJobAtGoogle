class Node(object):
	"""Defination of a single node of Linked List"""
	def __init__(self, value):
		self.value = value
		self.next = None
		

class LinkedList(object):
	"""
	Defination of a Linked List
	(This is head) ---> Node==>Node==>Node==>Node
	"""
	def __init__(self, head=None):
		super(LinkedList, self).__init__()
		self.head = head
		self.size = 1

		if self.head == None:
			self.size = 0




	"""
	Print the linked list
	"""
	def printList(self):
		current_node = self.head
		if self.head:
			while current_node:
				print(current_node.value)
				current_node = current_node.next


	"""
	This method adds an element at the end of Linked List.
	Here node_to_add is of type Node
	"""
	def append(self, node_to_add):
		# get the head of linked list
		current_node = self.head

		# if it is not an empty linked list
		if self.head:

			# traverse the linked list to the very end
			while current_node.next:
				current_node = current_node.next

			# add the new node at the very end
			current_node.next = node_to_add
			self.size += 1

		else:
			# if it is an empty linked list this new node is the of this linked list
			self.head = node_to_add


	"""
	Return the element at a certain position.
	If no such position exists, return None
	"""
	def get_from_position(self, position):

		if position < 1 or position > self.size:
			return None

		current_node = self.head

		if self.head:
			# do something
			counter = 1
			while current_node:
				if counter == position:
					return current_node
				current_node = current_node.next
				counter += 1
			return None

		else:
			return None

	"""
	Insert a node at a given position
	"""
	def insert(self, node, position):
		current_node = self.head

		if self.head:
			if position == 1:
				node.next = head
				head = node
				return
			counter = 1
			while current_node and counter < position:
				if counter == position -1:
					node.next = current_node.next
					current_node.next = node
				counter += 1
				current_node = current_node.next

			if counter < position:
				print('Position larger than Linked List')
				return
		else:
			print('Emty list!')

	"""
	Delete a node by value
	"""

	def delete(self, value):
		current_node = self.head

		if self.head.value == value:
			self.head = self.head.next
			return

		if self.head:
			previous_node = current_node
			while current_node:
				if current_node.value == value:
					previous_node.next = current_node.next
				previous_node = current_node
				current_node = current_node.next


		