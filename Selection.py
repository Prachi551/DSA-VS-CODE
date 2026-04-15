def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i   # assume first element is minimum

        # find minimum in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap minimum with current position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Example
arr = [8, 7, 1, 5, 3, 2, 9] 
print(selection_sort(arr))  