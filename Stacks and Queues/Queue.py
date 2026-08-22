class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        return self

    def dequeue(self):
        if self.head is None:
            raise Exception("queue is empty")
        former_head = self.head
        self.head = former_head.next
        former_head.next = None
        self._size -= 1
        if self._size == 0:
            self.tail = None
        return former_head.value

    def clear(self):
        self.head = self.tail = None
        self._size = 0
        return self

    def peek(self):
        if self.head:
            return self.head.value
        return None

q = Queue()

q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
q.enqueue(12)
q.enqueue(14)
q.enqueue(19)
q.enqueue(21)
q.enqueue(29)

print(len(q))
print(q.peek())

print(q.dequeue())
print(q.peek())
print(len(q))