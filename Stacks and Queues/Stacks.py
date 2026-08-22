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

    def pop(self):
        if not self._size:
            raise Exception("stack is empty")
        former_top = self._top
        self._top = former_top.next
        former_top.next = None
        self._size -= 1
        return former_top.value

    def peek(self):
        if self._top:
            return self._top.value
        return None

    def clear(self):
        self._top = None
        self._size = 0
        return self


s = Stack()

s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.push(10)
s.push(12)
s.push(14)
s.push(19)
s.push(21)
s.push(29)

print(len(s))
print(s.peek())

print(s.pop())
print(s.peek())
print(len(s))