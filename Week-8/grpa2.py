# The question looks like a geometry problem, but after sorting by the top coordinates (X1), it becomes an inversion-counting problem on the bottom coordinates (X2). Once you count the inversions, you have the number of line intersections.


def countIntersection(X1, X2):
    # Step 1: Pair up top and bottom x-coordinates and sort them based on X1
    pairs = sorted(zip(X1, X2), key=lambda item: item[0])

    # Extract the sequence of X2 values after sorting by X1
    arr = [item[1] for item in pairs]

    # Step 2: Count inversions in arr using Merge Sort in O(n log n) time
    def merge_and_count(arr, temp_arr, left, mid, right):
        i = left  # Starting index for left subarray
        j = mid + 1  # Starting index for right subarray
        k = left  # Starting index to be merged
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                # There is an inversion because arr[i] > arr[j]
                temp_arr[k] = arr[j]
                inv_count += mid - i + 1
                j += 1
            k += 1

        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        for idx in range(left, right + 1):
            arr[idx] = temp_arr[idx]

        return inv_count

    def merge_sort_and_count(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
            inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
            inv_count += merge_and_count(arr, temp_arr, left, mid, right)

        return inv_count

    n = len(arr)
    temp_arr = [0] * n
    return merge_sort_and_count(arr, temp_arr, 0, n - 1)