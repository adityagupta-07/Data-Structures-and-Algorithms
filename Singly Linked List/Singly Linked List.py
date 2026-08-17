class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def append(self, value):
        new_node = Node(value)
        if self._length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1
        return self

    def pop_left(self):
        if not self._length:
            raise Exception("list is empty")
        former_head = self.head
        self.head = former_head.next
        former_head.next = None
        self._length -= 1
        if not self._length:
            self.tail = None
        return former_head.value

a = SinglyLinkedList()  
 
a.append(5) 
a.append(9) 
a.append(14)
a.pop_left()


print(a.head.value)
print(a.tail.value)
print(a._length)