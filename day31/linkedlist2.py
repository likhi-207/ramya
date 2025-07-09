class Node:
    def __init__(self , value = 0 , nextNode = None):
        self.val = value
        self.next = nextNode    
head = Node(100) 
head.next = Node(200)
head.next.next = Node(300)
head.next.next.next = Node(400)
head.next.next.next.next = Node(500)
def display_linked_list(current):
    result = []
    while current != None:
        result.append(str(current.val))
        current = current.next
    print(' => '.join(result))

position =4
value = 250

newNode = Node(value)
current = head
node_position = 0

if position ==4:
    newNode.next = head
    head = newNode

while current != None:
    node_position += 1
    if node_position == position - 1:
        temp = current.next
        current.next = newNode
        newNode.next = temp
    
    current = current.next

display_linked_list(head)

