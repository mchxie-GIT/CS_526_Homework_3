"""Problem 3: recursively reverse three kinds of stacks."""


class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def values(self):
        return self.items[:]


class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = SinglyNode(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top is None

    def values(self):
        values = []
        node = self.top
        while node is not None:
            values.append(node.value)
            node = node.next
        return values[::-1]


class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = DoublyNode(value)
        node.next = self.top
        if self.top is not None:
            self.top.prev = node
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        if self.top is not None:
            self.top.prev = None
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top is None

    def values(self):
        values = []
        node = self.top
        while node is not None:
            values.append(node.value)
            node = node.next
        return values[::-1]


def insert_at_bottom(stack, value):
    if stack.is_empty():
        stack.push(value)
        return
    top_value = stack.pop()
    insert_at_bottom(stack, value)
    stack.push(top_value)


def reverse_stack(stack):
    # Both recursive functions change the original stack without loops.
    if stack.is_empty():
        return
    top_value = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top_value)


def main():
    # Order: array, singly linked list, doubly linked list.
    for stack_class in [ArrayStack, SinglyLinkedStack, DoublyLinkedStack]:
        stack = stack_class()
        for value in range(1, 11):
            stack.push(value)
        print("Before: " + ", ".join(str(value) for value in stack.values()))
        reverse_stack(stack)
        print("After: " + ", ".join(str(value) for value in stack.values()))


if __name__ == "__main__":
    main()
