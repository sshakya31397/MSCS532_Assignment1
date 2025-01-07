import random
import time
import sys
import tracemalloc

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Function to generate different datasets
def generate_data(size):
    random_data = [random.randint(1, 10000) for _ in range(size)]
    sorted_data = sorted(random_data)
    reverse_sorted_data = sorted_data[::-1]
    return random_data, sorted_data, reverse_sorted_data

# Function to record performance metrics
def measure_performance(sort_func, arr):
    tracemalloc.start()  # Start memory tracking
    start_time = time.time()  # Start timing
    sorted_arr = sort_func(arr)  # Sorting the array
    end_time = time.time()  # End timing
    current, peak = tracemalloc.get_traced_memory()  # Get memory usage
    tracemalloc.stop()  # Stop memory tracking
    execution_time = end_time - start_time  # Time taken to sort
    memory_usage = peak / 10**6  # Convert to MB
    return execution_time, memory_usage

# Comparing performance
sizes = [1000, 5000, 10000]  # Sizes of datasets to test
results = []

for size in sizes:
    random_data, sorted_data, reverse_sorted_data = generate_data(size)
    
    print(f"Running tests for size {size}:")
    
    for data_type, data in [("Random", random_data), ("Sorted", sorted_data), ("Reverse Sorted", reverse_sorted_data)]:
        print(f"  Testing {data_type} Data:")
        
        # Quick Sort
        quick_time, quick_memory = measure_performance(quick_sort, data)
        print(f"    Quick Sort: Time = {quick_time:.6f}s, Memory = {quick_memory:.6f}MB")
        
        # Merge Sort
        merge_time, merge_memory = measure_performance(merge_sort, data)
        print(f"    Merge Sort: Time = {merge_time:.6f}s, Memory = {merge_memory:.6f}MB")
    
    print()