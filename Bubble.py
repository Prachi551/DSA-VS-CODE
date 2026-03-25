def bubble_sort(arr):
    n = len(arr)

    # outer loop (passes)
    for i in range(n):

        # inner loop (comparison)
        for j in range(0, n - i - 1):

            # compare adjacent elements
            if arr[j] > arr[j + 1]:
                # swapping
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Example
arr = [8, 7, 1, 5, 3, 2, 9]
print(bubble_sort(arr))