import time

# Function to print the array at each step
def print_step(arr):
    print(arr)
    time.sleep(0.5)  # Slow down to watch the process

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    print("\n--- Bubble Sort ---")
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print_step(arr)

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            print_step(arr)

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            print_step(arr)

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            print_step(arr)

# Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print_step(arr)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Heap Sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print_step(arr)
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print_step(arr)
        heapify(arr, i, 0)

# Main program
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)

    choice = input("\nChoose sorting algorithm (bubble/merge/quick/heap): ").lower()

    if choice == "bubble":
        bubble_sort(arr)
    elif choice == "merge":
        merge_sort(arr)
    elif choice == "quick":
        quick_sort(arr, 0, len(arr) - 1)
    elif choice == "heap":
        heap_sort(arr)
    else:
        print("Invalid choice!")

    print("\nSorted array:", arr)
