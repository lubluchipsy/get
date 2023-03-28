# A Linked List Node
class Node:
	def __init__(self, data = None, next=None):
		self.data = data
		self.next = next


# Function to print a given linked list
def printList(head):
	ptr = head
	while ptr is not None:
		print(ptr.data, end = ' ')
		ptr = ptr.next




# Function to construct a linked list from a given set of keys
def construct(keys):
	head = None

	# start from the end of the list
	for i in reversed(range(len(keys))):
		# allocate a new node in a heap and set its data
		head = Node(keys[i], head)

	return head



keys = list(map(int, input().split()))
head = construct(keys)
element, replacement = map(int, input().split())


ptr = head

while ptr.data != element:
	ptr = ptr.next

ptr.data = replacement
printList(head)

