# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)


# ---- Test Code ----
if __name__ == "__main__":
    ll = LinkedList()

    # Insert 10, 20, 30
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)

    # Display the result
    ll.display()   # Expected output: Linked List: [10, 20, 30]