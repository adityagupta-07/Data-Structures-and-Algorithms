import math

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
    return array

def selection_sort(array):
    for i in range(len(array)):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]
    return array


def bubble_sort(array):
    for i in range(len(array) - 1):
        has_swapped = False
        for j in range(len(array) - 1, i, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                has_swapped = True
        if not has_swapped:
            break
    return array


def shell_sort(array):
    gaps = [5, 3, 1]
    for gap in gaps:
        for i in range(gap, len(array)):
            j = i - gap
            while array[j + gap] < array[j] and j >= 0:
                array[j], array[j + gap] = array[j + gap], array[j]
                j -= gap
    return array


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


def heap_sort(array):
    heapify(array)
    for end_idx in range(len(array) - 1, 0, -1):
        array[0], array[end_idx] = array[end_idx], array[0]
        move_down(array, 0, end_idx - 1)
    return array


def heapify(array):
    last_nonleaf_idx = len(array) // 2 - 1
    for i in range(last_nonleaf_idx, -1, -1):
        move_down(array, i, len(array) - 1)
    return array


def move_down(array, start_idx, end_idx):
    child_idx = 2 * start_idx + 1
    while child_idx <= end_idx:
        if child_idx < end_idx and array[child_idx] < array[child_idx + 1]:
            child_idx += 1
        if array[start_idx] < array[child_idx]:
            array[start_idx], array[child_idx] = array[child_idx], array[start_idx]
            start_idx = child_idx
            child_idx = 2 * start_idx + 1
        else:
            child_idx = end_idx + 1


def radix_sort(array):
    max_digits = get_max_number_of_digits(array)
    for i in range(max_digits + 1):
        buckets = [[] for _ in range(10)]
        for num in array:
            digit = get_digit_at_position(num, position=i)
            buckets[digit].append(num)
        array = flatten(buckets)
    return array


def get_max_number_of_digits(array):
    return max(int(math.log10(abs(num))) + 1 if num != 0 else 1 for num in array)


def get_digit_at_position(number, position):
    return (abs(number) // 10 ** position) % 10


def flatten(array):
    return [num for inner in array for num in inner]