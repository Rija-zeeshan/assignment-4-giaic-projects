def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find middle index
        if arr[mid] == target:
            return mid  # Element found at index mid
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return -1  # Element not found

# Example list (must be sorted)
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Ask user for number to search
num = int(input("Enter number to search: "))

result = binary_search(numbers, num)

if result != -1:
    print(f"Number found at index {result}.")
else:
    print("Number not found in the list.")
