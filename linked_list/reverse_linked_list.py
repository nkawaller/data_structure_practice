# References https://www.geeksforgeeks.org/reverse-a-linked-list/

# Node class

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

# Driver code
my_linked_list = LinkedList()
my_linked_list.push(1)
my_linked_list.push(2)
my_linked_list.push(3)
my_linked_list.push(4)
my_linked_list.push(5)

my_linked_list.printList()