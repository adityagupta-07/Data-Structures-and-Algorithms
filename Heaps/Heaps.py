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

    '''
    Sift-Up Algorithm (Max-Heap)

    1. Start at the last item in the heap (the one you just inserted).
    2. Find its parent. A node at index i has its parent at (i - 1) // 2.
    3. Compare the item with its parent.
    - If the item is smaller than or equal to the parent → heap rule satisfied → stop, you're done.
    - If the item is bigger than the parent → they're in the wrong order (max-heap rule broken) → swap them.
        - Make the swapped parent position the new current position (child_idx = parent_idx), and repeat from step 2.
    4. Keep repeating until either:
    - You reach the root (child_idx == 0), or
    - The item is no longer bigger than its parent.
    '''

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

    '''
    Remove-Max Algorithm (Max-Heap)

    1. Check if the heap is empty. If it is, raise an error — there's nothing to remove.
    2. Save the root value (index 0) — this is the maximum, and what you'll return at the end.
    3. Swap the root with the last item in the heap.
    4. Remove the last item from the heap (it's now the old root/max, sitting at the end — take it out).
    5. Sift down from the root — the item you just moved to the root is probably too small for its new spot, so let move_down() sink it into its correct position.
    6. Return the saved maximum value.
    '''

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

    '''
    Sift Down Algorithm (Max-Heap)

    1. Start at the root (index 0).
    2. Look at its children. A node at index i has children at 2i+1 (left) and 2i+2 (right).
    3. Find the bigger child. Compare left and right child — pick whichever is larger.
    4. Compare parent with the bigger child.
    - If the parent is smaller than that child → they're in the wrong order (max-heap rule broken) → swap them.
        - Make the swapped child the new parent (the position that received the value now becomes the parent), and repeat from step 2.
    - If the parent is bigger or equal → heap rule satisfied → stop, you're done.
    5. Keep repeating until either:
    - There's no child left (child_idx > end_idx), or
    - The parent is already bigger than its biggest child.
    '''


def heapify(array):
    last_parent_idx = len(array) // 2 - 1
    for parent_idx in range(last_parent_idx, -1, -1):
        last_idx = (len(array) - 1)
        move_down(array, parent_idx, last_idx)
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
            '''
            The old parent has moved to the child's old position after the swap.

            For example:
            Before swap:
                parent_idx = 0  -> old parent
                child_idx  = 1  -> old child

            After swap:
                old parent is now at index 1
                old child is now at index 0

            So, we need to update the index variable in our code.
                Update parent_idx to the old child's index:
                parent_idx = child_idx

            In simple terms:
                The old parent has moved to the child's position,
                so the old parent is now the child in the next step.

            If the old parent was at index 0 and the old child was at index 1,
            after they are swapped:
                old parent -> index 1
                old child  -> index 0

            But in our code, we need to update the variable that represents
            the old parent's new position.

            So:
                parent_idx = 1  (old child_idx's value)
            '''
            child_idx = 2 * parent_idx + 1 # find the left child of parent_idx down the heap
        else:
            break
'''
Sift-Down Algorithm (Max-Heap, array/heapsort version)

1. Start at start_idx.
2. Look at its children. A node at index i(start_idx) has children at 2i+1 (left) and 2i+2 (right).
3. Find the bigger child. Compare left and right child (only if the right child is within end_idx) — pick whichever is larger.
4. Compare the item at start_idx with the bigger child.
   - If the item is smaller than that child → they're in the wrong order (max-heap rule broken) → swap them.
     - Make the swapped child index the new start_idx, and repeat from step 2.
   - If the item is bigger or equal → heap rule satisfied → stop, you're done.
5. Keep repeating until either:
   - There's no child left within range (child_idx > end_idx), or
   - The item at start_idx is already bigger than its biggest child.
'''

h = MaxBinaryHeap()

h.insert(4)
h.insert(5)
h.insert(6)
h.insert(7)
h.insert(8)
h.insert(9)
h.insert(10)
h.insert(12)
h.insert(14)
h.insert(19)
h.insert(21)
h.insert(29)

print(h.items)

print(h.remove_max())
print(h.items)

arr = [4, 10, 3, 5, 1, 8, 9, 2, 7, 6]
print(heapify(arr))