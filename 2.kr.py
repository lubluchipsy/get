# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Function to print a given linked list
def printList(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end=' —> ')
        ptr = ptr.next

    print('None')


# Function to construct a linked list from a given set of keys
def construct(keys):
    head = None

    # start from the end of the list
    for i in reversed(range(len(keys))):
        # allocate a new node in a heap and set its data
        head = Node(keys[i], head)

    return head


# input keys
keys = list(input().split())

# points to the head node of the linked list
head = construct(keys)

conc = ''
ptr = head
while ptr is not None:
    conc += ptr.data
    ptr = ptr.next

if conc[::-1] == conc:
    print('Yes')
else:
    print('No')
