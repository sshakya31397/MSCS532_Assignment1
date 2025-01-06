def insertion_sort_decreasing(arr):
    # sort out the values in the arr starting from 1
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted
        j = i - 1  # Start comparing with the element before it
        
        # moving the elements of an array 
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # placing the key after the correct position
        arr[j + 1] = key

    return arr


arr = [1, 14, 22, 45, 71, 3, 15]
print("Original array:", arr)

sorted_arr = insertion_sort_decreasing(arr)
print("Sorted array in decreasing order:", sorted_arr)