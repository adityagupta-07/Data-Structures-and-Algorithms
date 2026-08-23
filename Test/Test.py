class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current:
            item = self.current.value
            self.current = self.current.next
            return item
        else:
            raise StopIteration
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
            return self._length

    def __iter__(self):
        return SinglyLinkedListIterator(self.head)

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
a.append(6)
a.append(7)
a.append(8)
a.append(9)
a.append(10)
a.append(12)
a.append(14)
a.append(19)
a.append(21)
a.append(29)

print(f"Number of nodes: {len(a)} \nHead: {a.head.value} \nTail: {a.tail.value}")


# Loop throught all the nodes and print value of each node:
# node = a.head
# while node:
#     print(node.value)
#     node = node.next
    
# Loop throught all the nodes and print value of each node (iterable class):
# node = a.head
# while node in a:
#     print(node.value)
#     node = node.next



for node in a:
    print(node)