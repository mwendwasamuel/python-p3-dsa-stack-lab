class Stack:
    def __init__(self, items=None, limit=100):
        # Initialize the stack with items and a limit.
        self.items = items if items is not None else []
        self.limit = limit

    def push(self, item):
        # Push an item onto the stack if it hasn't reached the limit.
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack Overflow")

    def size(self):
        # Return the number of elements in the stack.
        return len(self.items)

    def isEmpty(self):
        # Check if the stack is empty.
        return len(self.items) == 0

    def pop(self):
        # Pop an item from the stack if it's not empty.
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def full(self):
        # Check if the stack is full (reached the limit).
        return len(self.items) == self.limit

    def peek(self):
        # Return the top element of the stack if it's not empty.
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def search(self, target):
        # Search for an element in the stack and return its position (0-indexed) from the top.
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        else:
            return -1