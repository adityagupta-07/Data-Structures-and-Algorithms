class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList: # Defines SinglyLinkedList named class object in memory
    # SinglyLinkedList() creates new empty object {} and a is already pointing towards it
    def __init__(self):
        # now self also points towards the newly created object SinglyLinkedList {} and __init__ sets new attributes supplied below
        self.head = None
        self.tail = None
        self._length = 0
        #  __init__ creates attributes inside that empty object {} and makes it: {head=none, tail=none, _length=0}. a and self both are pointing towards this object

    def __len__(self):
        return self._length

    def append(self, value): # self = pointing towards SinglyLinkedList obj, value = 4
        # SinglyLinkedList is the newly created object with {head=none, tail=none, _length=0} 
        new_node = Node(value)
        # Here class Node declares class obj in memory and new_node creates new empty object {} from Node class object 
        # Then new_node is pointing towards node object {value=4, next=none} created from Node class 
        if self._length == 0: # SinglyLinkedList obj {head=none, tail=none, _length=0}
            self.head = self.tail = new_node # when _length=0, {head=none, tail=none, _length=0} becomes {head={value=4, next=none}, tail={value=4, next=none}, _length=0}
        else:
            # only if _length=1
            # {head={value=4, next=none}, tail={value=4, next=none}, _length=1}
            # new_node = {value=5, next=none}
            self.tail.next = new_node
            # {head={value=4, next=none}, tail={value=4, next={value=5, next=none}}, _length=1}
            self.tail = new_node
            # {head={value=4, next=none}, tail={value=5, next=none}, _length=1}
        self._length += 1 # {head={value=4, next=none}, tail={value=5, next=none}, _length=2}
        return self 

a = SinglyLinkedList() # SinglyLinkedList() creats new empty object {} from class SinglyLinkedList and then a points towards that newly made object
 
a.append(4) 
# SinglyLinkedList.append(a, 4)
a.append(5) 
# SinglyLinkedList.append(a, 5) 
 