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

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

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
it = iter(a)
while True:
    try:
        print(next(it))
    except StopIteration:
        break



# for node in a: 
#     print(node) 