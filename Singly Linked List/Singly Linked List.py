class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# class LinkedListIterator:
#     def __init__(self, head):
#         self.current = head

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if not self.current:
#             raise StopIteration
#         else:
#             item = self.current.value
#             self.current = self.current.next
#             return item

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
        return self._length

    # def __iter__(self):
    #     return LinkedListIterator(self.head)

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

    def pop_right(self):
        if not self._length:
            raise Exception("list is empty")
        tail_value = self.tail.value
        if self._length == 1:
            self.head = self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = None
        self._length -= 1
        return tail_value

    def remove(self, value):
        if not self._length:
            raise Exception("list is empty")
        if self.head.value == value:
            return self.pop_left()
        if self.tail.value == value:
            return self.pop_right()
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            raise ValueError("item not in list")
        if current_node.next is None:
            self.tail = previous_node
        previous_node.next = current_node.next
        current_node.next = None
        self._length -= 1
        return current_node.value

    def reverse(self):
        if self._length < 2:
            return self
        left_node = None
        middle_node = self.head
        while middle_node is not None:
            right_node = middle_node.next
            middle_node.next = left_node
            left_node = middle_node
            middle_node = right_node
        self.head, self.tail = self.tail, self.head
        return self

    def traverse(self, head):
        node = head
        while node:
            print(f"{node.value} → ")
            node = node.next
        return
    

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

print(len(a))
print(a.head.value, a.tail.value)

# a.traverse(a.head)


# Loop through the nodes and print the value of each node
# node = a.head
# while node in a: # we need to make class iterable to execute this
#     print(node)
#     node = node.next

# Loop through the nodes and print the value of each node
node = a.head
while node is not None: # we don't need to make class iterable to execute this
    print(node.value)
    node = node.next

# for node in a:
#     print(node)

# a = iter(a)
# print(a)

# head = next(a)
# node = head
# while node:
#     print(node.value)
#     node = next(a)

# node = a.head
# while node is not None:
#     print(node.value)
#     node = node.next