class MaxBinaryHeap:
    def __init__(self):
        self.items = []

    def insert(self, value):
        self.items.append(value)
        self.move_up()
        return self

    def move_up(self):
        child_idx = len(self.items) - 1
        while child_idx > 0:
            parent_idx = (child_idx - 1) // 2
            if self.items[child_idx] <= self.items[parent_idx]:
                break
            self.swap(child_idx, parent_idx)
            child_idx = parent_idx 

    def swap(self, idx_1, idx_2):
        self.items[idx_1], self.items[idx_2] = self.items[idx_2], self.items[idx_1]

    def remove_max(self):
        if not self.items:
            raise Exception("Heap is empty")
        max_elem = self.items[0]
        end_idx = len(self.items) - 1
        self.swap(0, end_idx)
        self.items.pop()
        self.move_down()
        return max_elem 

    def move_down(self):
        parent_idx = 0
        child_idx = 2 * parent_idx + 1
        end_idx = len(self.items) - 1
        while child_idx <= end_idx:
            if child_idx < end_idx and self.items[child_idx] < self.items[child_idx + 1]:
                child_idx += 1
            if self.items[parent_idx] < self.items[child_idx]:
                self.swap(parent_idx, child_idx)
                parent_idx = child_idx
                child_idx = 2 * parent_idx + 1
            else:
                break

def heapify(array):
    last_parent_idx = len(array) // 2 - 1
    for parent_idx in range(last_parent_idx, -1, -1):
        move_down(array, parent_idx, last_idx = (len(array) - 1))
    return array

def move_down(array, parent_idx, last_idx):
    child_idx = 2 * parent_idx + 1 # left child
    while child_idx <= last_idx:  # Sometimes the parent maybe a leaf. So this checks if parent's child is in the array or not
        # Now we need to select the bigger child (left or right)
        if child_idx < last_idx: # means there is right child to compare
            if array[child_idx] < array[child_idx + 1]: # if left child is smaller than right child
                child_idx += 1 # select right child
        if array[parent_idx] < array[child_idx]: # if parent is smaller than child
            array[parent_idx], array[child_idx] = array[child_idx], array[parent_idx] # swap parent and child
            # values has been swapped, so update the index variables in our code
            parent_idx = child_idx # old child_idx = 1, so we updated the position of new parent in our code.
            child_idx = 2 * parent_idx + 1 # find the left child of parent_idx down the heap
        else:
            break 