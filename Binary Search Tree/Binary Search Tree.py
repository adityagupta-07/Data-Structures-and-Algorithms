class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return self
        current_node = self.root
        while value != current_node.value:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                current_node = current_node.right
        return self

    def contains(self, value):
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return True
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    @staticmethod
    def _get_successor(current):
        successor = current.right
        while successor and successor.left:
            successor = successor.left
        return successor

    def _remove_node_no_children(self, current, parent):
        if current is self.root:
            self.root = None
            return self
        if parent.left == current:
            parent.left = None
        else:
            parent.right = None
        return self
    
    def _remove_node_one_child(self, current, parent):
        if current is self.root:
            self.root = current.right if current.right else current.left
            return self
        if parent.right == current:
            parent.right = current.right if current.right else current.left
        else:
            parent.left = current.right if current.right else current.left
        return self

    def _remove_node_two_children(self, current):
        successor = self._get_successor(current)
        current.value = successor.value
        return self.remove(successor.value, start=current.right, parent=current)

    def remove(self, value, start=None, parent=None):
        current = start or self.root
        while current and current.value != value:
            parent = current
            if value < current.value:
                current = parent.left
            else:
                current = parent.right
        if not current:
            raise Exception("item not in tree")
        if not current.right and not current.left:
            return self._remove_node_no_children(current, parent)
        if current.right and current.left:
            return self._remove_node_two_children(current)
        return self._remove_node_one_child(current, parent)


a = BinarySearchTree()

a.insert(4)
a.insert(5)
a.insert(6)
a.insert(7)
a.insert(8)
a.insert(9)
a.insert(10)
a.insert(12)
a.insert(14)
a.insert(19)
a.insert(21)
a.insert(29)

print(a.contains(12))
a.remove(12)
print(a.contains(12))