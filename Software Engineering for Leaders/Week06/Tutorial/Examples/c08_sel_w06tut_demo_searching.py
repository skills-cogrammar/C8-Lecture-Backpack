# ============== Binary Search Iteratively and Recursively

# Step 1 − Initialise two pointers: 
#          left = 0 (start of the list) and right = len(lst) - 1 (end of the list).
# Step 2 − Calculate the middle index: mid = (left + right) // 2.
# Step 3 − Compare the element at mid (lst[mid]) with the target key:
#          - If lst[mid] == key, return the mid index (key found).
#          - If lst[mid] < key, move the left pointer to mid + 1 (search in the right half).
#          - If lst[mid] > key, move the right pointer to mid - 1 (search in the left half).
# Step 4 − Repeat steps 2 and 3 while left <= right.
# Step 5 − If the loop ends without finding the key, return -1 (key not found).

def binary_search(lst, key):
    """
    Perform binary search to find the index of the given key in the sorted list.

    Parameters:
        lst (list): The sorted list to be searched.
        key: The value to be searched for in the list.

    Returns:
        int: The index of the key in the list if found, otherwise -1.
    """
    # Initialise left pointer to the beginning of the list.
    left = 0
    # Initialise right pointer to the end of the list.
    right = len(lst) - 1

    # Loop until left pointer is less than or equal to the right pointer.
    while left <= right:
        # Calculate the middle index.
        mid = (left + right) // 2

        # If the middle element is equal to the key, return its index.
        if lst[mid] == key:
            return mid
        
        # If the middle element is less than the key, update left pointer 
        # to search in the right half.
        if lst[mid] < key:
            left = mid + 1
        # If the middle element is greater than the key, update right pointer 
        # to search in the left half.
        else:
            right = mid - 1

    # If the key is not found in the list, return -1.
    return -1

def binary_search_recursive(lst, min_pt, max_pt, key):
    # Base case: If the range is invalid, return -1 (key not found)
    if min_pt > max_pt:
        return -1
    
    mid = (min_pt + max_pt) // 2  # Find the middle index
    
    # If the key is found at mid, return the index
    if lst[mid] == key:
        return mid
    # If the key is smaller than mid, search in the left half
    elif lst[mid] > key:
        return binary_search_recursive(lst, min_pt, mid - 1, key)
    # If the key is larger than mid, search in the right half
    else:
        return binary_search_recursive(lst, mid + 1, max_pt, key)

# ------- Test the binary search
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
min_idx = 0
max_idx = len(lst) - 1

print(binary_search_recursive(lst, min_idx, max_idx, 9))  # Output: 8 (index of key=9)
print(binary_search_recursive(lst, min_idx, max_idx, 10))  # Output: -1 (10 not in list)


# ============== Linear Search Iteratively

# Step 1 − Start at the first element of the list (index 0).
# Step 2 − Compare the current element with the target key:
#          - If the current element is equal to the key, return the index (key found).
#          - If not, move to the next element.
# Step 3 − Repeat Step 2 for each element in the list.
# Step 4 − If you reach the end of the list without finding the key, return -1 (key not found).

def linear_search(lst, key):
    """
    Perform linear search to find the index of the given key in the list.

    Parameters:
        lst (list): The list to be searched.
        key: The value to be searched for in the list.

    Returns:
        int: The index of the key in the list if found, otherwise -1.
    """
    # Iterate through the list.
    for i in range(len(lst)):
        # If the current element is equal to the key, return its index.
        if lst[i] == key:
            return i
    # If key is not found in the list, return -1.
    return -1

# ------- Test the linear search
lst = [1,2,3,4,5,6,7,8,9]
key_to_search = 9

# Perform linear search on the list to find the index of key 9 and print the result.
print(linear_search(lst, key_to_search))
