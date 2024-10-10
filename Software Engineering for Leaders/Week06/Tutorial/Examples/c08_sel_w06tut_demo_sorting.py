# =============  Bubble sort - O(n^2)

# Step 1 − Check if the first element in the input array is 
#          greater than the next element in the array.
# Step 2 − If it is greater, swap the two elements; otherwise move 
# the pointer forward in the array.
# Step 3 − Repeat Step 2 until we reach the end of the array.
# Step 4 − Check if the elements are sorted; if not, repeat the same process (Step 1 to Step 3) 
#          from the last element of the array to the first.
# Step 5 − The final output achieved is the sorted array.

def bub_sort(lst):
    """
    Perform bubble sort to sort the given list in ascending order.

    Parameters:
        lst (list): The list to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    # Iterate through the list.
    for i in range(len(lst)):
        num_swaps = 0
        # Iterate through the unsorted (left) portion of the list.
        for j in range(0, len(lst)-i-1):
            # If the current element is greater than the next element, swap them.
            if lst[j] > lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]		# Swap the values
                num_swaps = 1
        # If no swaps were made in this pass, the list is already sorted.
        if num_swaps == 0:
            break
    # Return the sorted list.
    return lst

# ------ Test the sort
lst = [5,3,2,9,6,1]
bubble_sort_lst = bub_sort(lst)

print(f"Your sorted list is: {bubble_sort_lst}")

# =============  Insertion sort - O(n^2)

# Step 1 − If it is the first element, it is already sorted. return 1;
# Step 2 − Pick next element
# Step 3 − Compare with all elements in the sorted sub-list
# Step 4 − Shift all the elements in the sorted sub-list that is greater than 
#          the value to be sorted
# Step 5 − Insert the value
# Step 6 − Repeat until list is sorted

def ins_sort(lst):
    # Loop through the array starting from the second element
    for i in range(1, len(lst)):

        # Store the current element in a variable 'key'
        key = lst[i]

        # Initialise a variable 'j' to point to the element before the current one
        j = i - 1

        # Move elements of 'lst[0..i-1]', that are greater than 'key', to one position ahead of their current position
        while j >= 0 and lst[j] >= key:

            lst[j + 1] = lst[j]
            j = j - 1

        # Place 'key' into its correct position in the sorted subarray
        lst[j + 1] = key

    return lst

# ------ Test the sort
lst = [5,3,2,9,6,1]
insertion_sort_lst = ins_sort(lst)

print(f"Your sorted list is: {insertion_sort_lst}")

# ============= Selection sort - O(n^2)

# Step 1 − Set MIN to location 0.
# Step 2 − Search the minimum element in the list.
# Step 3 − Swap with value at location MIN.
# Step 4 − Increment MIN to point to next element.
# Step 5 − Repeat until the list is sorted.

def sel_sort(lst):
    """
    Perform selection sort to sort the given list in ascending order.

    Parameters:
        lst (list): The list to be sorted.

    Returns:
        list: The sorted list in ascending order.
    """
    # Iterate through the list.
    for i in range(len(lst)):
        # Assume the current index contains the minimum value.
        min_value_idx = i
        # Iterate through the unsorted portion of the list to find the 
        # index of the minimum value.
        for j in range(i+1, len(lst)):
            # If a smaller value is found, update the index of the minimum value.
            if lst[j] < lst[min_value_idx]:
                min_value_idx = j
        # Swap the current element with the minimum value found.
		lst[i], lst[min_value_idx] = lst[min_value_idx], lst[i]
    # Return the sorted list.
    return lst

# ------ Test the sort
lst = [5,3,2,9,6,1]
selection_sort_lst = sel_sort(lst)

print(f"Your sorted list is: {selection_sort_lst}")

"""
Other sort methods are:
Quick Sort, Merge Sort, Heap Sort, Tim Sort, Radix Sort

Summary:
- Best for general cases: Quick Sort - O(n log n)).
- Best when stability is needed: Merge Sort or Timsort - O(n log n).
- Best for large numbers or fixed-length data: Radix Sort - (O(nk) where

"""