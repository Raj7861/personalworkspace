
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def insert_beg(head: Node, data) -> Node:
    newNode = Node(data)
    newNode.next = head
    head = newNode
    
    return head

def insert_end(head: Node, data: int):
    new_node = Node(data)

    while head.next != None:
        head = head.next
    head.next = new_node

def print_node(head: Node):

    while head.next != None:
        print(head.data)
        head = head.next
    print(head.data)

head = Node(200)
insert_end(head, 300)
insert_end(head, 400)
head = insert_beg(head,700)
head = insert_beg(head,90000)

print_node(head)


# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class linked_list:
#     def __init__(self, data) -> None:
#         self.head = Node(data)

#     def insert_beg(self,data) -> Node:
#         newNode = Node(data)
#         newNode.next = self.head
#         self.head = newNode

#     def insert_end(self, data: int):
#         new_node = Node(data)
#         curr = self.head
#         while curr.next != None:
#             curr = curr.next
#         curr.next = new_node

#     def print_node(self):
#         curr = self.head
#         while curr.next != None:
#             print(curr.data)
#             curr = curr.next
#         print(curr.data)
