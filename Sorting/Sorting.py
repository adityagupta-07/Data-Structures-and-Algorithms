import math

def insertion_sort(array):
    for i in range(1, len(array)): # start at second element array[i]
        j = i # j will help to compare with the element on the left using array[j-1]
        while j > 0 and array[j - 1] > array[j]: # when left element > current element, and j > 0 as j -= 1 and j>0 check tells "you've reached the front of the array, stop! and there's nothing on the left to compare with" and while loop stops
            array[j - 1], array[j] = array[j], array[j - 1] # swap left element and current element
            j -= 1 # go one index back and repeat -> (compare with left child, swap with it, again go one element back, compare with ITS left child, swap with it, again go one element back...)
    return array # SORTED!!!

'''
INSERTION SORT
1. Start from the second element (index 1) — the first element alone is already "sorted."
2. Let j = i (current position).
3. Check j > 0 if j is already 0, stop; nothing to the left to compare with.
4. If j > 0, compare array[j-1] (left neighbor) with array[j] (current element).
5. If left neighbor > current element, swap them.
6. Move one step left (j -= 1) and go back to step 3.
7. Stop when j reaches 0, or when left neighbor <= current element.
8. Move to the next i and repeat until the whole array is scanned.
9. Array is sorted.
'''


def selection_sort(array):
    last_idx = len(array)
    for i in range(last_idx): # starts with i = 0 automatically by default (when the start isn't defined)
        smallest = i # assume first element is smallest
        for j in range(i + 1, last_idx = len(array)): # starts at index 1 (i+1 = 0+1 = 1), so j = 1 in the starting
            if array[j] < array[smallest]: # if second element is smaller than smallest element (first/left most element)
                smallest = j # remember that lesser element
        array[i], array[smallest] = array[smallest], array[i] # swap them
    return array

'''
SELECTION SORT
Example: [10 59 23 70 11 42 17 31 95 20]
1.  Start at the first position i = 0
2.  Consider the value to be the smallest, i = smallest = 0 index 
3.      Start from one element on the right, i + 1 (j = i + 1).
4.      Compare it(array[j]) with the element with smallest tag(array[smallest])
        If it(array[j]) is smaller:
        Remember its index in smallest variable(smallest = j).
        Loop continue and jump to line 3 and it will start with the element on the more right (i + 2 for explanation)
        This way, it will find and remember the index of smallest value in [59 23 70 11 42 17 31 95 20]
5.  After searching and going through the elements one by one in [59 23 70 11 42 17 31 95 20]:
        The varible smallest will remember the index of smallest value in [59 23 70 11 42 17 31 95 20]
        And the element with current postition array[i] will get swapped with the smallest element(array[smallest]).
6.  Move to the next position, for i will go to array[i = 1] position and again for j will start from i + 1(element right to i).
7.  Jump to for j again (line 3)  
8.  Repeat until the entire array is sorted.
9.  Return the array.
'''

def bubble_sort(array):
    for i in range(len(array) - 1): 
        # len(array) = 4
        # Valid indexes are:
        # 0, 1, 2, 3
        # But we compare:
        # array[j] with array[j + 1] -> array[3] and array[4]
        # Therefore j cannot be 3, because:
        # j + 1 = 4 → index 4 does not exist.
        # The largest valid j is 2 -> array[2] and array[3]
        # So we need:
        # range(3)
        # which gives:
        # j = 0, 1, 2
        # So now array[2] and array[3] are comparable
        for j in range(len(array) - 1 - i):
            # 1st iteration: [10, 5, 8, 2]
            # 2nd iteration: [5, 10, 8, 2]
            # 3rd iteration: [5, 8, 10, 2]
            # 4th iteration: [5, 8, 2, 10]
            if array[j] > array[j + 1]: # array[0] > array[1] = 10 > 5
                array[j], array[j + 1] = array[j + 1], array[j] # swap them, [10, 5, 8, 2] becomes [5, 10, 8, 2]
                # So in this block, the greatest element will be sent to the last.
                # After 2nd iteration of for i, second largest element will be at second last position.
                # That's why (len(array) - 1 - i) is used which just says "ignore the sorted part"
        # After each pass of for i block, an element at the end is already sorted. For example, in 1st iteration, we will have 10 at the end, in 2nd iteraion, we will have 8, 10 at the end.
        # That's why we can just skip the end part which is already sorted using "for j in range(len(array) - 1 - i)"
        # 1st iteration: [5, 8, 2, 10]
        # 2nd iteration: [5, 2, 8, 10]
        # 3rd iteration: [2, 5, 8, 10]
    return array

'''
BUBBLE SORT
Example: [10, 5, 8, 2]
1.  Start from the first element.
2.  Compare the current element with the element immediately to its right.
3.  If the current element is greater than the element on its right:
        Swap them.
4.  Move to the next position on the right and compare the next pair.
5.  Continue comparing the elements on the right until reaching the end of the array. 
6.  After one complete pass (completion of for j loop block):
        The largest unsorted element will have moved/bubbled to the end of the array.
7.  Start another pass from the beginning (for i block 2nd iteration).
8.  On each new pass, ignore the elements that are already sorted at the end.
9.  Repeat the process until the entire array is sorted.
10. Return the array.
'''

def shell_sort(array):
    gaps = [5, 3, 1]
    for gap in gaps:
        last_idx = len(array)
        for i in range(gap, last_idx):
            current = i
            while current >= gap and array[current] < array[current - gap]:
                # current >= gap ensures that an element exists gap positions to the left. This help ensure if the swapping can be done or not with the current element.
                array[current], array[current - gap] = array[current - gap], array[current]
                current -= gap
    return array

'''
SHELL SORT
Example: [10 59 23 70 11 42 17 31 95 5]
1. Create a list of gaps.
       gaps = [5, 3, 1]
2. Take the first gap from the gaps list.
       Example: gap = 5
3. Start the for i loop from the gap index.
       i = gap
   This ensures that there is an element gap positions to the left of the current element.
4. Store the current position in a variable:
       current = i
5. Check whether:
       current >= gap
   This ensures that an element exists gap positions to the left of the current element.
6. Also check whether:
       array[current] < array[current - gap]
   This checks whether the current element is smaller than the element gap positions to its left.
7. If both conditions are true:
       Swap array[current] and array[current - gap].
8. After the swap, move the current position backwards by the gap:
       current = current - gap
9. Repeat the while loop while:
       current >= gap
       AND
       array[current] < array[current - gap]
10. When the while loop finishes, move the for i loop to the next element on the right.
11. Continue until all elements have been processed for the current gap.
12. Move to the next gap.
       5 → 3 → 1
13. Repeat the same process for each gap.
14. When gap = 1:
       Compare elements that are immediately next to each other.
15. After completing the gap = 1 pass, the entire array is sorted.
16. Return the array.
'''

def merge_sort(array):
    if len(array) < 2:
        return array
    first_half = merge_sort(array[:len(array) // 2]) 
    second_half = merge_sort(array[len(array) // 2:])
    return merge(first_half, second_half)

def merge(first_half, second_half):
    result = []
    i = j = 0
    while i < len(first_half) and j < len(second_half):
        if first_half[i] < second_half[j]:
            result.append(first_half[i])
            i += 1
        else:
            result.append(second_half[j])
            j += 1
    while i < len(first_half):
        result.append(first_half[i])
        i += 1
    while j < len(second_half):
        result.append(second_half[j])
        j += 1
    return result

'''
MERGE
Example:
first_half  = [5, 10]
second_half = [2, 8]
1. Create an empty result list.
2. Create two pointers:
       i = 0
       j = 0
   i points to the current element of first_half.
   j points to the current element of second_half.
3. Compare first_half[i] with second_half[j].
4. Add the smaller element to result.
5. Move the pointer of the array from which
   the element was taken one position forward.
6. Continue comparing the elements while
   both halves still have elements.
7. When one half becomes empty:
       Add all remaining elements from the other half
       to result.
8. Return result.
'''


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    return partition(arr, 0, len(arr) - 1)

def partition(array, start, end):
    if start >= end:
        return
    pivot = end
    boundary = start
    for i in range(start, end):
        if array[i] <= array[pivot]:
            array[boundary], array[i] = array[i], array[boundary]
            boundary += 1
    array[boundary], array[end] = array[end], array[boundary]
    partition(array, start, boundary - 1)
    partition(array, boundary + 1, end)
    return array

'''
QUICK SORT — PARTITION
Example:
[10, 5, 8, 2, 7]
1. Start with the portion of the array that needs to be sorted.
2. If start >= end:
       Stop.
   This means the portion contains zero or one element
   and is therefore already sorted.
3. Choose the last element as the pivot.
       pivot = end
4. Set boundary equal to start.
       boundary = start
   The boundary represents the position where the next
   element smaller than or equal to the pivot should go.
5. Start the i loop from start and stop before end.
6. Look at array[i].
7. Compare array[i] with the pivot.
8. If array[i] <= pivot:
       Swap array[i] with array[boundary].
9. Move boundary one position to the right.
       boundary += 1
10. Continue checking every element before the pivot.
11. After all elements have been checked:
       Swap the pivot with array[boundary].
12. The pivot is now in its correct final position.
13. Everything to the left of the pivot is <= pivot.
14. Everything to the right of the pivot is > pivot.
15. Recursively call partition() on the left portion.
       start → boundary - 1
16. Recursively call partition() on the right portion.
       boundary + 1 → end
17. Continue partitioning until every portion has
    zero or one element.
18. Return the sorted array.
'''

def heap_sort(array):
    heapify(array)
    for end_idx in range(len(array) - 1, 0, -1):
        array[0], array[end_idx] = array[end_idx], array[0]
        move_down(array, 0, end_idx - 1)
    return array

def heapify(array):
    last_parent_idx = len(array) // 2 - 1
    last_idx = len(array) - 1
    for parent_idx in range(last_parent_idx, -1, -1):
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
            child_idx = 2 * parent_idx + 1 # find the left child of parent_idx down the heap
        else:
            break

'''
HEAP SORT
Example: [10, 5, 8, 2, 7, 3]
1. Call heapify(array) to convert the array into a max heap.
2. After heapify:
       The largest element will be at index 0.
3. Start a loop from the last index of the array and move toward index 1.
       end_idx = len(array) - 1 → 1
4. Swap the element at index 0 with the element at end_idx.
       The largest element is now placed at the end of the unsorted portion.
5. The element at end_idx is now in its final sorted position.
6. Reduce the unsorted portion by moving end_idx one position to the left.
7. Call move_down(array, 0, end_idx - 1).
       This restores the max-heap property for the remaining unsorted portion.
8. Repeat the process:
       Swap the largest element from index 0 with the last unsorted element.
       Move the end position one step left.
       Restore the max heap using move_down().
9. Continue until end_idx reaches 1.
10. At this point, all elements are in their correct positions.
11. Return the sorted array.
'''

def radix_sort(array):
    max_digits = get_max_number_of_digits(array)
    for i in range(max_digits + 1):
        buckets = [[] for _ in range(10)]
        for num in array:
            digit = get_digit_at_position(num, position=i)
            buckets[digit].append(num)
        array = flatten(buckets)
    return array

# def get_max_number_of_digits(array):
#     return max(int(math.log10(abs(num))) + 1 if num != 0 else 1 for num in array)

def get_max_number_of_digits(array):
    max_digits = 0
    for num in array:
        if num == 0:
            digits = 1
        else:
            digits = int(math.log10(abs(num))) + 1 
        if digits > max_digits:
            max_digits = digits
    return max_digits

'''
1. Start with max_digits = 0.
2. Go through every number.
3. Find how many digits that number has.
4. If it has more digits than max_digits, update max_digits.
5. After checking all numbers, return max_digits.

'''

# def get_digit_at_position(number, position):
#     return (abs(number) // 10 ** position) % 10

def get_digit_at_position(number, position):
    number = abs(number)
    divisor = 10 ** position
    digit = (number // divisor) % 10
    return digit

'''
GET DIGIT AT POSITION
Example: number = 5837, position = 2
1. Take the absolute value of the number.
       This removes the negative sign if the number is negative.
2. Calculate 10 raised to the given position.
       divisor = 10 ** position
3. Divide the number by the divisor using integer division.
       number // divisor
       This removes the digits to the right of the required digit.
4. Take the remainder when dividing the result by 10.
       result % 10
       This gives the digit at the required position.
5. Return the digit.
'''

# def flatten(array):
#     return [num for inner in array for num in inner]

def flatten(array):
    result = []
    for inner_array in array:
        for num in inner_array:
            result.append(num)
    return result

'''
FLATTEN
Example:
array = [[1, 4], [2, 5], [3, 6]]
1. Create an empty result list.
2. Go through each inner array one by one.
3. For each inner array:
       Go through each number inside it.
4. Add each number to the result list.
5. Continue until all inner arrays and all their elements have been processed.
6. Return the result list.
'''