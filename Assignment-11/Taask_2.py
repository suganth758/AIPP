class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


# ---- Test Examples ----
if __name__ == "__main__":
    q = Queue()

    # Test enqueue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print("After enqueues:", q.items)  # ['A', 'B', 'C']

    # Test dequeue()
    print("Dequeue:", q.dequeue())  # A
    print("After dequeue:", q.items)  # ['B', 'C']

    # Test is_empty()
    print("Is empty?", q.is_empty())  # False

    # Remove all items
    q.dequeue()
    q.dequeue()

    print("Is empty after removing all?", q.is_empty())  # True
