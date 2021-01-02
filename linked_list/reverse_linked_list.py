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
            print(temp.data, end='')
            temp = temp.next
        print('\n')

    # def reverse(self):
    #     prev = None
    #     current = self.head
    #     while(current is not None):
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
    #     self.head = prev 

    """ trying to figure this way out"""
    def reverse(self):
        prev, head = None, self.head
        while head:
            head.next, prev, head = prev, head, head.next

# Driver code
my_linked_list = LinkedList()
my_linked_list.push(1)
my_linked_list.push(2)
my_linked_list.push(3)
my_linked_list.push(4)
my_linked_list.push(5)

my_linked_list.printList()
my_linked_list.reverse()
my_linked_list.printList()
