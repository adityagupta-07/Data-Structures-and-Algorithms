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

a = SinglyLinkedList() 
a.append(4)
a.append(5)
 