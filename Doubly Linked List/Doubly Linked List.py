class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self._length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self._length += 1
        return self

    def pop_left(self):
        if not self._length:
            raise Exception("list is empty")
        former_head = self.head
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.head = former_head.next
            former_head.next = None
            self.head.previous = None
        self._length -= 1
        return former_head.value

    def pop_right(self):
        if not self._length:
            raise Exception("list is empty")
        former_tail = self.tail
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.tail = former_tail.previous
            former_tail.previous = None
            self.tail.next = None
        self._length -= 1
        return former_tail.value

    def remove(self, value):
        if not self._length:
            raise Exception("list is empty")
        if self.head.value == value:
            return self.pop_left()
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            raise ValueError("item not in list")
        if current_node.next is None:
            return self.pop_right()
        current_node.next.previous = previous_node
        previous_node.next = current_node.next
        current_node.previous = None
        current_node.next = None
        self._length -= 1
        return current_node.value



a = DoublyLinkedList()

a.append(4)
a.append(5)
a.append(6)
a.append(8)
a.append(9)

print(a.head.value)
print(a.tail.value)
print(a._length)

a.remove(9)

print(a._length)
