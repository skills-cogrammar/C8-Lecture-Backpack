import random
import time

def insertion_sort(array):
    """Sorts an array using the Insertion Sort algorithm.

    Args:
        array (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    i = 1
    length = len(array)
    while i < length:
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
        i = i + 1
    return array


def selection_sort(array):
    """Sorts an array using the Selection Sort algorithm.

    Args:
        array (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    length = len(array)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


def bubble_sort(array):
    """Sorts an array using the Bubble Sort algorithm.

    Args:
        array (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    length = len(array)
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, length - 1):
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
                swapped = True
    return array


def linear_search(arr, target):
    """Searches for a target value in an array using Linear Search.

    Args:
        arr (list): The list to search through.
        target: The value to search for.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """Searches for a target value in a sorted array using Binary Search.

    Args:
        arr (list): The sorted list to search through.
        target: The value to search for.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Test the algorithms

small_list = [34, 7, 23, 32, 5, 62, 32, 1, 12, 45]
print("Insertion Sort:", insertion_sort(small_list.copy()))
print("Selection Sort:", selection_sort(small_list.copy()))
print("Bubble Sort:", bubble_sort(small_list.copy()))

large_list = random.sample(range(1, 101), 100)

start_time = time.time()
insertion_sort(large_list.copy())
print("Insertion Sort Time:", time.time() - start_time)

start_time = time.time()
selection_sort(large_list.copy())
print("Selection Sort Time:", time.time() - start_time)

start_time = time.time()
bubble_sort(large_list.copy())
print("Bubble Sort Time:", time.time() - start_time)

sorted_small_list = sorted(small_list)
target = 32
print("Linear Search (target 32):", linear_search(small_list, target))
print("Binary Search (target 32):", binary_search(sorted_small_list, target))

large_list_for_search = random.sample(range(1, 101), 100)
sorted_large_list = sorted(large_list_for_search)
target_large = sorted_large_list[50]

start_time = time.time()
linear_search_result = linear_search(large_list_for_search, target_large)
print("Linear Search Result:", linear_search_result)
print("Linear Search Time:", time.time() - start_time)

start_time = time.time()
binary_search_result = binary_search(sorted_large_list, target_large)
print("Binary Search Result:", binary_search_result)
print("Binary Search Time:", time.time() - start_time)