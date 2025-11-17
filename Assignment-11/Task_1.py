class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


# -----------------------
# Test Examples
# -----------------------
if __name__ == "__main__":
    s = Stack()

    # Test push()
    s.push(1)
    s.push(2)
    s.push(3)
    print("After pushes:", s.items)  # [1, 2, 3]

    # Test peek()
    print("Peek:", s.peek())  # 3

    # Test pop()
    print("Pop:", s.pop())  # 3
    print("After pop:", s.items)  # [1, 2]

    # Test is_empty()
    print("Is empty?", s.is_empty())  # False

    # Pop remaining items
    s.pop()
    s.pop()
    print("Is empty after popping all?", s.is_empty())  # True
