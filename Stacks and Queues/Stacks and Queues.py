class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0
        self._max_allowed_size = 100

    def __len__(self):
        return self._size

    def push(self, value):
        if self._max_allowed_size == self._size:
            raise Exception("stack size limit exceeded")
        new_element = Node(value)
        new_element.next = self._top
        self._top = new_element
        self._size += 1
        return self